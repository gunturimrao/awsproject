from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from . import views
from django.conf.urls import url

app_name = 'testapp'

urlpatterns = [
    # path("", views.testing, name='test'),
    path('', views.register, name='register'),
    path('register/', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    path('email/', views.email, name='email'),
    path('sucess/', views.sucess, name='sucess'),
    path('upload/', views.upload, name='upload')

]
