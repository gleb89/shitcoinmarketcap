from celery import shared_task


    
@shared_task
def sample_task():
    try:
        from apps.coins import service
        service.get_update_price_coins()
    except:
        print('error')








   