
from django.urls import path, include
import blogapp.views
import album.views
from . import views

urlpatterns = [

path('<int:blog_id>', blogapp.views.detail, name = "detail"),
path('new/',blogapp.views.new,name="new"),
path('create', blogapp.views.create, name ="create"),
path('newblog/',blogapp.views.blogpost,name="newblog"),
]