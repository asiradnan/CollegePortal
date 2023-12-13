from django.contrib import admin
from .models import CLASS,Student,Teacher,Department,ContactNumber,Principal


admin.site.register(CLASS)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(ContactNumber)
admin.site.register(Principal)