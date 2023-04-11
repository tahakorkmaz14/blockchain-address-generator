from django.urls import path
from django.contrib import admin
from core import views as core_views
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view()),
    path('generate-address/', core_views.WalletAPIView.as_view()),
    path('list-address/', core_views.listAddress),
    path('retreive-address/<str:pk>', core_views.getAddress),
]
