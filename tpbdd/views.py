from django.shortcuts import render
from tpbdd.models import DatabaseData
#from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def homepage(request):
	return HttpResponse("Here is the data.")

#def sender(request, data):
#	return HttpResponse("Data send : %s" % data)