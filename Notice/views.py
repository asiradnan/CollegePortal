from django.shortcuts import render,redirect
from .forms import NoticeForm
from .models import Notice


def notice_home(request):
    notices = Notice.objects.all()
    return render(request,'Notice/notice_home.html', {'notices':notices})
def make_notice(request):
    if request.method=="POST":
        form  = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.posted_by=request.user
            notice.save()
            return redirect('Notice:notice')
    else:
        form = NoticeForm
    return render(request, 'Notice/notice_form.html',{'form':form})
