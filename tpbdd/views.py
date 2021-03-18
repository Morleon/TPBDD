from django.shortcuts import render
from tpbdd.models import DatabaseData
from django.http import HttpResponse
from django.template import loader
from pyope.ope import OPE
import random

def homepage(request):
	data = DatabaseData.objects.order_by('number')[:10]
	encrypted_data = DatabaseData.objects.values('key','number').order_by('number')
	decrypted_data = {'key':'value'}
	cipher = OPE(b'mDErfp0Arn+noGTR+p0P9CmGU8+KKenk8ff+6aHxPi0=')
	for x in encrypted_data:
		x["number"] = cipher.decrypt(x["number"])
	context = {'data': data, 'encrypted_data': encrypted_data}
	return render(request, 'index.html', context)

def insertion(request):
	print(request.POST)
	cipher = OPE(b'mDErfp0Arn+noGTR+p0P9CmGU8+KKenk8ff+6aHxPi0=')
	for i in range(1, 10): 
 		value = random.randrange(1, 10000)
 		value = cipher.encrypt(value)
 		data_instance = DatabaseData.objects.create(key=i, number=value)
	return render(request, "insertion.html")