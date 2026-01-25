from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
<<<<<<< HEAD
def home(request):
    return HttpResponse("welcome to task manngement system")
def contact(request):
    return HttpResponse("Welcome")

=======

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")


def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")
>>>>>>> module-5
