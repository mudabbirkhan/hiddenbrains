from celery import shared_task
from django.core.mail import send_mail


email_subject = "Registration"
email_body = "You are successfully registered Thank You!!!"
email_from = "sender@example.com"
email_to = "receiver@example.com"


@shared_task
def send_register_email():
    send_mail(email_subject, email_body, email_from, [email_to, ])
    return 'Success! Mail Sent'
