from django.urls import path
from . import views

app_name = 'Academics'

urlpatterns=[
    path('student/',views.student,name='student'),
    path('teacher/',views.teacher,name='teacher'),
    path('department/',views.department,name='department'),
    path('principal/',views.principal,name='principal'),
    path('AddingClass/',views.add_class,name='add_class'),
    path('Departments/',views.departments,name='departments'),
    path('Classes/',views.classes,name='classes'),
    path('profile/',views.user_profile,name='user_profile'),
    path('profile/update_student_profile',views.update_student_profile,name='update_student_profile'),
    path('profile/update_teacher_profile',views.update_teacher_profile,name='update_teacher_profile'),
    path('profile/update_principal_profile',views.update_principal_profile,name='update_principal_profile'),
    path('Departments/<name>/',views.dept_detail,name='dept_detail'),
    path('Classes/<class_code>/',views.class_detail,name='class_detail'),
    path('make_captain/<int:student_id>/', views.make_captain, name='make_captain'),
    path('profile/add_contact/', views.add_contact, name='add_contact'),
    path('detail/<int:user_id>', views.student_profile, name='student_profile'),
]
