from django.shortcuts import render
from django.core.mail import send_mail



def send_mail2(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(
            f'connect with {title}',
            
            f'text {message}',
            
            'noreply@somehost.local',
            
            [email]
        )
    return render(request, 'gamil.html')