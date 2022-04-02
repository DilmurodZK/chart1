from django.urls import path
from .views import *

urlpatterns = [
    path('', base),
    path('example/', example),
    path('index/', index),
    path('yaim/', yaim),

    
]