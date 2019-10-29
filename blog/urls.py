from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about),
    path('policy/', views.policy),
    path('contact/', views.contact),
    path('tnc/', views.tnc),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]