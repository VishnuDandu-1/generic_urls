from django.urls import path
from mobile.views import samsung

urlpatterns=[
    path('samsung/',samsung,name='samsung')
]