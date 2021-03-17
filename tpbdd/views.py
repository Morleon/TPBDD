from django.shortcuts import render
from tpbdd.models import DatabaseData
#from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def homepage(request):
	data = DatabaseData.objects.order_by('-number')[:10]
	context = {'data': data}
	#query_results = YourModel.objects.all()
	return render(request, 'index.html', context)

def insertion(request):
	#return render("The database has been added")
	return HttpResponse("The database has been initialised")

#def sender(request, data):
#	return HttpResponse("Data send : %s" % data)