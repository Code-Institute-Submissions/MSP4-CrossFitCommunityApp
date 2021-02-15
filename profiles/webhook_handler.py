from django.http import HttpResponse
from .views import createDefaultHeroLevels
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import time
from datetime import datetime


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, new_profile):
        """ Send the user a confirmation email"""
        print("SENDING EMAIL")
        cust_email = new_profile.email
        subject = render_to_string(
            'profiles/confirmation_emails/account_created_subject.txt',
            {'profile': new_profile})
        body = render_to_string(
            'profiles/confirmation_emails/account_created_body.txt',
            {'profile': new_profile, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        userprofile = intent.metadata
        birthdate = datetime.strptime(userprofile.birthdate, "%d %b %Y")
        birthdate = datetime.strftime(birthdate, "%Y-%m-%d")
        user = User.objects.get(pk=userprofile.user)
        print(user)
        profile_exists = False
        attempt = 1
        while attempt <= 5:
            print("IN WHILE")
            try:
                new_profile = UserProfile.objects.get(
                    # full_name__iexact=userprofile.full_name,
                    # town_or_city__iexact=userprofile.town_or_city,
                    # country__iexact=userprofile.country,
                    # gender__iexact=userprofile.gender,
                    # weight__iexact=userprofile.weight,
                    # birthdate__iexact=birthdate,
                    user=user,
                    # stripe_pid__iexact=pid
                )
                profile_exists = True
                print("PROFILE IS TRUE")
                break
            except UserProfile.DoesNotExist:
                print("NOT FOUND: Retry in 1 second")
                attempt += 1
                time.sleep(1)
        if profile_exists:
            print("NO ERROR: PROFILE EXISTS")
            self._send_confirmation_email(new_profile)
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | \
                        Success: Verified profile already in database',
                    status=200)
        else:
            print("PROFILE NOT FOUND: CREATE IN WEBHOOK")
            new_profile = None
            try:
                new_profile = UserProfile.objects.create(
                    full_name=userprofile.full_name,
                    town_or_city=userprofile.town_or_city,
                    email=user.email,
                    country=userprofile.country,
                    gender=userprofile.gender,
                    weight=userprofile.weight,
                    birthdate=birthdate,
                    user=user,
                    stripe_pid=pid
                )
                new_profile.image = 'media/noprofpic.jpg'
                new_profile.save()
                createDefaultHeroLevels(user)
            except Exception as e:
                print("in the exception")
                if new_profile:
                    print("deleting profile because of error")
                    new_profile.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(new_profile)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | \
                SUCCESS: created profile in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
