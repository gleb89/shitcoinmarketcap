from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt import views as jwt_views

from apps.coins.views import CoinsViewSet, CoinsPaginationViewSet, ExchangeViewSet
from apps.users.views import UserCreate
from apps.comments.views import CommentsViewSet

router = routers.DefaultRouter()
router.register(r'coins', CoinsPaginationViewSet, basename='Coinspaginator')
router.register(r'coinslist', CoinsViewSet, basename='Coins')
router.register(r'user', UserCreate, basename='User')
router.register(r'comments', CommentsViewSet, basename='Commentsr')
# router.register(r'exchange', ExchangeViewSet, basename='Exchange')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/admin/', admin.site.urls),
    path('api/openapi/', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
