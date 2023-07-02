#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import json

import stripe

from core.settings import STRIPE_API_KEY

# from flask import redirect, jsonify, json, request


class StripeSubscriptionsService():
    customer_email = None
    price_id = None
    domain_app = 'http://localhost:4242'

    def __init__(self, domain_url, customer_email):
        stripe.api_key = STRIPE_API_KEY
        self.domain_app = domain_url
        self.customer_email = customer_email

    def set_price_from_product_id(self, product_id):
        price = stripe.Price.list(product=product_id, limit=1)
        self.price_id = price.data[0].id

    def create_checkout_session(self):
        success_url = self.domain_app + \
            '?success=true&session_id={CHECKOUT_SESSION_ID}'
        cancel_url = self.domain_app + '?canceled=true'
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price': self.price_id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url=success_url,
            cancel_url=cancel_url,
            customer_email=self.customer_email
        )
        return checkout_session

    # https://dashboard.stripe.com/webhooks
    def webhook_received(self, request):
        secret = 'whsec_12345'
        request_data = json.loads(request.data)
        payload = request.data
        if secret:
            # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
            sig_header = request.headers.get('stripe-signature')
            try:
                event = stripe.Webhook.construct_event(
                    payload,
                    sig_header,
                    secret
                )
                data = event['data']
            except Exception as e:
                return e
            # Get the type of webhook event sent - used to check the status of PaymentIntents.
            event_type = event['type']
        else:
            data = request_data['data']
            event_type = request_data['type']
        data_object = data['object']

        print('event ' + event_type)

        if event_type == 'checkout.session.completed':
            print('🔔 Payment succeeded!')
        elif event_type == 'customer.subscription.trial_will_end':
            print('Subscription trial will end')
        elif event_type == 'customer.subscription.created':
            print('Subscription created %s', event.id)
        elif event_type == 'customer.subscription.updated':
            print('Subscription created %s', event.id)
        elif event_type == 'customer.subscription.deleted':
            print('Subscription canceled: %s', event.id)

        return json.dumps({'status': 'success'})

    # @app.route('/create-portal-session', methods=['POST'])
    # def customer_portal():
    #     # For demonstration purposes, we're using the Checkout session to retrieve the customer ID.
    #     # Typically this is stored alongside the authenticated user in your database.
    #     checkout_session_id = request.form.get('session_id')
    #     checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)

    #     # This is the URL to which the customer will be redirected after they are
    #     # done managing their billing with the portal.
    #     return_url = self.domain_app

    #     portalSession = stripe.billing_portal.Session.create(
    #         customer=checkout_session.customer,
    #         return_url=return_url,
    #     )
    #     return redirect(portalSession.url, code=303)
