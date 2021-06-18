import django
django.setup()

from celery import shared_task
from config.celery import app as celery_app

from .service import get_update_price_coins

@celery_app.task
def gettts():
    get_update_price_coins()


