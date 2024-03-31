from django.urls import path
from games.views import pubg
urlpatterns = [
    path('pubg/',pubg,name='pubg')
]