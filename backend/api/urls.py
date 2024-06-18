from django.urls import path
from .views import *

urlpatterns=[
    path('test', test),
    path('user', create_user),
    path('login', login_user),
    path('createword', create_word),
    path('getword', get_word),
    path('do', do)
]
