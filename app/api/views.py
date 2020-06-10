from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .__init__ import ml
from .models import Customer
from .serializers import CustomerSerializers
# from .forms import CustomerForm
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import json


def home(request):
    return HttpResponse("Bank App")

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


@api_view(['POST'])
@parser_classes([JSONParser])
def get_result(request):
    try:
        data = {k:[v] for (k,v) in request.data.items()}
        res = ml.predict(data=data)
        print(res)
        return JsonResponse('Your Status is {}'.format(res), safe=False)
    except:
        pass