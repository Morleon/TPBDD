from django.shortcuts import render
from tpbdd.models import DatabaseData
#from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader
from pyope.ope import OPE
import random

# Create your views here.
def homepage(request):
	data = DatabaseData.objects.order_by('number')[:10]
	context = {'data': data}
	#query_results = YourModel.objects.all()
	return render(request, 'index.html', context)

def insertion(request):
	print(request.POST)
	cipher = OPE(b'mDErfp0Arn+noGTR+p0P9CmGU8+KKenk8ff+6aHxPi0=')
	for i in range(1, 10): 
 		value = random.randrange(1, 10000)
 		value = cipher.encrypt(value)
 		data_instance = DatabaseData.objects.create(key=i, number=value)
	return render(request, "insertion.html")

#def sender(request, data):
#	return HttpResponse("Data send : %s" % data)