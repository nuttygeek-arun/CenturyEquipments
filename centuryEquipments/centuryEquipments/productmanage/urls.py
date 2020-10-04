from django.urls import include,path
from rest_framework import routers
from . import views

routers=routers.DefaultRouter()
routers.register(r'products',views.ProductViewSet)
urlpatterns = [
    path('', include(routers.urls)),
    path('api_auth/', include('rest_framework.urls',namespace='rest_framework')),
]