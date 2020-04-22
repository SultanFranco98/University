from django.urls import path, include
from .systems import *

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('ajax/load-specialitys/', load_specialitys, name='ajax_load_specialitys'),
    path('ajax/load-groups/', load_groups, name='ajax_load_groups'),
]