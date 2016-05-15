from django.shortcuts import render
from django.views.generic import ListView
from .models import Ticket
from .models import LoanApplication
# Create your views here.

class TicketList(ListView):
    model = Ticket
    template_name = "home.html"

    
#def home(request) :
	#return render(request,'home.html',{'title':'Welcome Home','user':'kshetty'})
	

class LoanApplicationDetails(ListView):
    model = LoanApplication
    template_name = "loanapplicationdetails.html"
    
class TicketDetails(ListView):
    model = Ticket
    template_name = "ticketdetails.html"
