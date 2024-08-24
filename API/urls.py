from django.urls import path
from .views import *

appname = 'API'

urlpatterns = [
    path('', peopleAPIView.as_view())
]
