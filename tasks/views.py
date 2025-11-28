from django.shortcuts import render
from django.http import HttpResponse

# Home View
def home_view(request):
    return render(request,"dashboard.html")

# Contact View
def contact_view(request):
    return HttpResponse("This is the contact page. Reach us at contact@taskmanagement.com")

# Create your views here.
