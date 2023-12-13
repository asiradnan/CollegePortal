from django.urls import path
from . import views

app_name = 'PostsNQueries'

urlpatterns=[
    path('',views.PnQ_home,name='PnQ_home'),
    path('create/',views.create_post,name='create_post'),
    path('add_comment/<int:post_serial>/', views.add_comment, name='add_comment')
]