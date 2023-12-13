from django.shortcuts import render,redirect
from .forms import StudentForm, TeacherForm, DepartmentForm, PrincipalForm, ClassForm,ContactForm
from .models import CLASS, Department,Student

def student(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        form2 = ContactForm(request.POST)
        if form.is_valid() and form2.is_valid() :
            user=form.save(commit=False)
            user.user=request.user
            user.save()
            user= form2.save(commit=False)
            user.user=request.user
            user.save()
            return redirect('home')
    else:
        form = StudentForm
        form2 = ContactForm
    return render(request, 'Academics/student.html',{'form':form,'form2':form2}) 

def teacher(request):
    if request.method=='POST':
        form = TeacherForm(request.POST)
        form2 = ContactForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user=form.save(commit=False)
            user.user=request.user
            user.save()
            user= form2.save(commit=False)
            user.user=request.user
            user.save()
            return redirect('home')
    else:
        form = TeacherForm
        form2 = ContactForm
    return render(request, 'Academics/teacher.html',{'form':form,'form2':form2}) 

def department(request):
    if request.method=='POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Academics:departments')
    else:
        form = DepartmentForm
    return render(request, 'Academics/department.html',{'form':form}) 

def principal(request):
    if request.method=='POST':
        form = PrincipalForm(request.POST)
        form2 = ContactForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user=form.save(commit=False)
            user.user=request.user
            user.save()
            user= form2.save(commit=False)
            user.user=request.user
            user.save()
            return redirect('home')
    else:
        form = PrincipalForm
        form2 = ContactForm
    return render(request, 'Academics/principal.html',{'form':form,'form2':form2}) 

def add_class(request):
    if request.method=='POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClassForm
    return render(request, 'Academics/add_class.html',{'form':form}) 
def classes(request):
    obj=CLASS.objects.all()
    return render(request,'Academics/classes.html',{'classes':obj})
def departments(request):
    obj=Department.objects.all()
    return render(request,'Academics/departments.html',{'departments':obj})

def user_profile(request):
    return render(request, 'Academics/user_profile.html')

def update_student_profile(request):
    profile = request.user.student
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('Academics:user_profile')
    else:
        form = StudentForm(instance=profile)
    return render(request, 'Academics/update_student_profile.html',{'form':form})

def update_teacher_profile(request):
    profile = request.user.teacher
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('Academics:user_profile')
    else:
        form = TeacherForm(instance=profile)
    return render(request, 'Academics/update_teacher_profile.html',{'form':form})


def update_principal_profile(request):
    profile = request.user.principal
    if request.method == 'POST':
        form = PrincipalForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('Academics:user_profile')
    else:
        form = PrincipalForm(instance=profile)

    return render(request, 'Academics/update_principal_profile.html',{'form':form})

def dept_detail(request,name):
    dept=Department.objects.get(name=name)
    return render(request,'Academics/dept_detail.html',{'dept':dept})

def class_detail(request,class_code):
    c=CLASS.objects.get(class_code=class_code)
    return render(request,'Academics/class_detail.html',{'class':c})

def make_captain(request, student_id):
    student = Student.objects.get(user_id=student_id)
    if request.user.teacher:
        student.make_captain()
        return redirect('Academics:class_detail', class_code=student.CLASS.class_code)
    return redirect('Academics:class_detail', class_code=student.CLASS.class_code)
    
def add_contact(request):
    if request.method=="POST":
        form =ContactForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.user=request.user
            user.save()
            return redirect('Academics:user_profile')
    else:
        form = ContactForm
    return render(request,"Academics/add_contact.html",{'form':form})

def student_profile(request,user_id):
    student=Student.objects.get(user_id=user_id)
    if request.user.teacher:
        return render(request,'Academics/student_profile.html',{'student':student})
    return render(request,'Academics/student_profile.html',{'student':student})
        
