from django.urls import path
from food.views import haleem

app_name='something'

urlpatterns=[
    path('haleem/',haleem,name='haleem')
]