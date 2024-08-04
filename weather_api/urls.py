from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name="home"),
    path("result/", views.result, name="result"),
     path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    # path('social_links', views.social_links),
]
