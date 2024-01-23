from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('all_albums/', views.all_albums, name='all_albums'),
    path('all_songs/', views.all_songs, name='all_songs'),

]
