from django.urls import path
from . import views 

app_name = 'Notice'

urlpatterns=[
    path('',views.notice_home,name='notice'),
    path('create/',views.make_notice,name='make_notice')
]