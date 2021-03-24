from django.shortcuts import render
from tpbdd.models import DatabaseData
from django.http import HttpResponse
from django.template import loader
from pyope.ope import OPE
import random

def homepage(request):
	data = DatabaseData.objects.order_by('number')[:10]
	
	if data :
		encrypted_data = DatabaseData.objects.values('key','number').order_by('number')
		cipher = OPE(b'mDErfp0Arn+noGTR+p0P9CmGU8+KKenk8ff+6aHxPi0=')

		for x in encrypted_data:
			x["number"] = cipher.decrypt(x["number"])

		context = {'data': data, 'encrypted_data': encrypted_data}
	else:
		context = {}
	return render(request, 'index.html', context)

def insertion(request):
	print(request.POST)
	cipher = OPE(b'mDErfp0Arn+noGTR+p0P9CmGU8+KKenk8ff+6aHxPi0=')
	for i in range(1, 10): 
		value = random.randrange(1, 10000)
		value = cipher.encrypt(value)
		data_instance = DatabaseData.objects.create(key=i, number=value)
	return render(request, "insertion.html")

def comparate(request, number1=1, number2=1):
	data = DatabaseData.objects.order_by('number')[:10]
	encrypted_data = DatabaseData.objects.values('key','number').order_by('number')
	display = ""
	number1 = encrypted_data[number1]["number"]
	number2 = encrypted_data[number2]["number"]

	if number1 == number2 :
		display = "the number are equals"
	if number1 < number2:
		display = "The first number is lower than the second number"
	if number2 < number1:
		display = "The second number is lower than the first number"

	context = {'number1': number1, 'number2': number2, 'display': display}
	return render(request, "comparate.html", context)

def add(request, number1=1, number2=1):
	data = DatabaseData.objects.order_by('number')[:10]
	encrypted_data = DatabaseData.objects.values('key','number').order_by('number')
	number1 = encrypted_data[number1]["number"]
	number2 = encrypted_data[number2]["number"]
	result = number1 + number2
	context = {'number1': number1, 'number2': number2, 'result': result}
	return render(request, "add.html", context)