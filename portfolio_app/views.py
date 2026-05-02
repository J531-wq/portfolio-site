from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'base.html', {'projects': projects})

def contact_view(request):
    projects = Project.objects.all()
    message_sent = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(
            subject="New Contact Form Submission",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["coderjoe16@gmail.com"],
            fail_silently=False,
        )
        message_sent = True

    return render(request, "base.html", {"projects": projects, "message_sent": message_sent})
