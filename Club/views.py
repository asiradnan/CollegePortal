from django.shortcuts import render,redirect
from .forms import ClubForm, MembershipForm
from .models import Club,Membership

from django.contrib import messages
def club_home(request):
    clubs=Club.objects.all()
    return render(request, 'Club/club_home.html',{'clubs':clubs})
def club_reg(request):
    if request.method=="POST":
        form  = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Club:club_home')
    else:
        form = ClubForm
    return render(request, 'Club/club_reg.html',{'form':form})

def membership(request):
    if request.method=="POST":
        form  = MembershipForm(request.POST)
        if form.is_valid():
            existing_membership = Membership.objects.filter(student=request.user.student, club=form.cleaned_data['club']).exclude(pk=form.instance.pk)
            if existing_membership.exists():
                messages.error(request, 'You are already a member of this club.')
                return redirect("Club:club_home")
            membership = form.save(commit=False)
            membership.student=request.user.student
            membership.save()
            messages.success(request, 'Successfully joined the club!')
            return redirect("Club:club_home")
            #redirect to the deatiled view of registered club
    else:
        form = MembershipForm
    return render(request, 'Club/membership.html',{'form':form})

def club_detail(request,club_name):
    memberships=Membership.objects.filter(club__club_name=club_name)
    club=Club.objects.get(club_name=club_name)
    return render(request, 'Club/club_detail.html',{'memberships':memberships,'club':club})