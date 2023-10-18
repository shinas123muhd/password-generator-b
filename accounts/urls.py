from django.contrib import admin
from django.urls import path
from .views import Generate,SavePasswords,ShowPasswords

urlpatterns = [
    
    path('generate/',Generate.as_view(),name = 'generate'),
    path('savepassword/',SavePasswords.as_view(),name='savepassword'),
    path('showpasswords/',ShowPasswords.as_view(),name='showpasswords'),
]