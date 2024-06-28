from django.urls import path
#from .views import index # - da forma abaixo, puxa todas as views!!
from . import views

# urlpatterns = [
#     path('home/', index, name='index')
# ]

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(),  name='post_detail'),
]