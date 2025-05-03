from django.contrib import admin
from django.urls import path,include
from core import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'register', views.RegisterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
]
