from django.urls import path
from . import views

app_name = 'Club'

urlpatterns=[
    path('',views.club_home,name='club_home'),
    path('create/',views.club_reg,name='club_reg'),
    path('membership/',views.membership,name='membership'),
    path('<club_name>/',views.club_detail,name='club_detail'),
]


