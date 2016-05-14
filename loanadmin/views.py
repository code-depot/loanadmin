from django.shortcuts import render
from django.views.generic import ListView
from .models import Ticket
# Create your views here.

class TicketList(ListView):
    model = Ticket
    template_name = "home.html"

    
def home(request) :
	return render(request,'home.html',{'title':'Welcome Home','user':'kshetty'})