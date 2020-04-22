from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', UsersLoginView.as_view(), name='login'),
    path('logout/', UsersLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)