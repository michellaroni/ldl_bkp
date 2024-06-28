from django.urls import path
from .views import raml

urlpatterns = [
    path('raml/', raml, name='raml')
]