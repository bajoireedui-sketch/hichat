from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Message, Profile, GroupSpace

def inbox_view(request):
    return render(request, 'inbox.html')

def messages_view(request, user_id=None):
    users = User.objects.exclude(id=request.user.id) if request.user.is_authenticated else User.objects.all()
    
    active_user = None
    messages = []
    
    if request.user.is_authenticated:
        if user_id:
            active_user = get_object_or_404(User, id=user_id)
        elif users.exists():
            active_user = users.first()
            
        if request.method == 'POST' and active_user:
            content = request.POST.get('content')
            if content:
                msg = Message.objects.create(
                    sender=request.user,
                    receiver=active_user,
                    content=content
                )
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({
                        'status': 'ok',
                        'content': msg.content,
                        'timestamp': msg.timestamp.strftime('%H:%M'),
                        'sender': msg.sender.username
                    })
                return redirect('messages_with_user', user_id=active_user.id)

        if active_user:
            messages = Message.objects.filter(
                sender=request.user, receiver=active_user
            ) | Message.objects.filter(
                sender=active_user, receiver=request.user
            )
            messages = messages.order_by('timestamp')

    context = {
        'users': users,
        'active_user': active_user,
        'messages': messages,
    }
    return render(request, 'messages.html', context)

def groups_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            group = GroupSpace.objects.create(
                name=name,
                description=description
            )
            if request.user.is_authenticated:
                group.members.add(request.user)
            return redirect('groups')

    groups = GroupSpace.objects.all()
    return render(request, 'groups.html', {'groups': groups})

def contacts_view(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
    else:
        profiles = Profile.objects.all()
    
    return render(request, 'contacts.html', {'profiles': profiles})

def settings_view(request):
    return render(request, 'settings.html')