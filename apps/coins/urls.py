from django.urls import path, include

from .views import (
 redirect_home_on_admin
)


urlpatterns = [
    path('', redirect_home_on_admin, name='homepage')
]