from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

def home(request):
    return render(request, 'portfolio/index.html')

def portfolio_details(request):
    return render(request, 'portfolio/portfolio-details.html')

def portfolio_details_2(request):
    return render(request, 'portfolio/portfolio-details-2.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Construct the email content
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL, 
                recipient_list=['sepehr779977@yahoo.com'],  
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent. Thank you!')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')

        return redirect('home')  

    return render(request, 'portfolio/index.html')