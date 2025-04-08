from django.shortcuts import render


def home(request):
    return render(request,'CollegePortal/homepage.html')

def about(request):
    return render(request,'CollegePortal/about.html')
def contact_us(request):
    return render(request,'CollegePortal/contact_us.html')