from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_otp_email(email, otp):
    subject = "Your OTP Code"
    
    html_content =render_to_string('otp_email.html',{"otp":otp})
    
    email_message =EmailMultiAlternatives(
        subject=subject,
        body="Your OTP is" + otp,
        to=[email]
    )
    
    email_message.attach_alternative(html_content,'text/html')
    email_message.send()