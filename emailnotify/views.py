from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from emailnotify.forms import SubscribeForm

def subscribe(request):
    form = SubscribeForm()

    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Greetings'
            message = 'Thank you for subscribing to our newsletter!'
            recipient = form.cleaned_data.get('email')
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                messages.success(request, 'Mail sent successfully')
            except Exception as e:
                messages.error(request, f"Failed to send email: {e}")
            return redirect('subscribe')

    return render(request, 'home.html', {'form': form})
