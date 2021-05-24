
from django.contrib import contenttypes
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                        verbose_name='User коментария',
                                on_delete=models.CASCADE)
    text_comment = models.TextField(verbose_name='текст коментария')
    parent = models.ForeignKey('self',
                                verbose_name='Родительский коментарий',
                                        blank=True,
                                        null=True,
                                        related_name='children' ,
                                        on_delete=models.CASCADE  
                                        )
    user_parent = models.IntegerField('Юсер коментария родителя',blank=True,null=True)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

