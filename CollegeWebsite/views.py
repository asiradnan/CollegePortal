from django.shortcuts import render


def home(request):
    return render(request,'CollegeWebsite/homepage.html')

def about(request):
    return render(request,'CollegeWebsite/about.html')
def contact_us(request):
    return render(request,'CollegeWebsite/contact_us.html')