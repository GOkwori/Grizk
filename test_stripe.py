import stripe
import os

# Set these to your actual keys
stripe.api_key = os.getenv(
    'STRIPE_SECRET_KEY', 'sk_test_51PSAGPCTx0frYLWS2V2RfBHnJKktvhj0BhtLshjkulfP7w4y0hXzTg4DS5JBIa5ofxi4n8VRd6EHKJ9mAVvLxEAy00LldlSUtx')

try:
    balance = stripe.Balance.retrieve()
    print(f"Stripe API connection successful. Balance: {balance}")
except stripe.error.AuthenticationError as e:
    print(f"Authentication with Stripe's API failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
