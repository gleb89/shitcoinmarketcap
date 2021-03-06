from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt import views as jwt_views

from apps.coins.views import (
                                CoinsViewSet,
                                CoinsPaginationViewSet,
                                ExchangeViewSet,
                                CoinsNewViewSet,
                                snippet_list,
                                redirect_home_on_admin
                                )
from apps.users.views import UserCreate
from apps.comments.views import CommentsViewSet

router = routers.DefaultRouter()
router.register(r'coins', CoinsPaginationViewSet, basename='Coinspaginator')
router.register(r'coinslist', CoinsViewSet, basename='Coins')
router.register(r'user', UserCreate, basename='User')
router.register(r'comments', CommentsViewSet, basename='Commentsr')
router.register(r'exchange', ExchangeViewSet, basename='Exchange')
router.register(r'updatecoins', CoinsNewViewSet, basename='updatecoins')




urlpatterns = [
     path('',redirect_home_on_admin,name='redirect_admin'),
     path('', include('apps.coins.urls')),
     path('api/v1/', include(router.urls)),
     path('api/admin/', admin.site.urls),
     path('api/openapi/', get_schema_view(
          title="Your Project",
          description="API for all things …",
          version="1.0.0"
     ), name='openapi-schema'),
     path('api/update/<str:name>/', snippet_list,
          name='updatetokendata'),
     path('api/login/', jwt_views.TokenObtainPairView.as_view(),
          name='token_obtain_pair'),
     path('api/ref/', jwt_views.TokenRefreshView.as_view(),
          name='token_refresh'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
