from django.db import models
from django.urls import reverse

from django.contrib.contenttypes.fields import GenericRelation
from apps.comments.models import Comments

class Exchange(models.Model):
    name = models.CharField('Название рынка', max_length=255)
    image = models.CharField('Изображение биржи', max_length=255, null=True)
    slug = models.SlugField('slug', max_length=100)
    trade_url = models.CharField('link', max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('еxchange:slug', kwargs={'slug': self.slug})

    class Meta:
        
        verbose_name = 'Рынок'
        verbose_name_plural = 'Рынки'



class Coins(models.Model):
    symbol         = models.CharField('Символ  монеты', max_length=55, null=True)
    name           = models.CharField('Название монеты', max_length=255)
    description    = models.TextField('Описание монеты', blank=True, null=True)
    image = models.CharField('Изображение монеты', max_length=255, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    price          = models.DecimalField('Цена', max_digits=12, decimal_places=10)
    market_cap = models.FloatField('Капитализация', blank=True, null=True)
    volume = models.TextField('Обьемы', blank=True, null=True)
    market_exchange = models.ManyToManyField(
                                            Exchange,
                                            related_name="market_list",
                                            verbose_name='торгуется на рынках',
                                            blank=True
                                            
                                            )
    price_exc = models.CharField('Изменение % 24ч', max_length=255,blank=True, null=True)
    board_price =  models.JSONField(encoder=None)
    comments = GenericRelation(Comments)
    
    

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Coin'
        verbose_name_plural = 'Coins'


class Note(models.Model):
    """
    A note consists of some text, and 0 or more descriptive tags.
    """
    text = models.CharField(max_length=1000)
    tags = GenericRelation(Comments)
