from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()

router.register(r'Shop', views.ShopViewSet)
router.register(r'Product', views.ProductViewSet)
router.register(r'ItemOrder', views.OrderItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]