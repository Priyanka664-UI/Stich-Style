import razorpay
from app.config.settings import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET))

def create_order(amount: int, currency: str = "INR"):
    data = {"amount": amount * 100, "currency": currency}
    return client.order.create(data=data)
