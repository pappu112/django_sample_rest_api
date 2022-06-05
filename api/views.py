from functools import partial
import json
import re
from django.http import JsonResponse
from urllib3 import HTTPResponse
from yaml import serialize
from .models import Students
from .serializers import StudentsSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.db import IntegrityError
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# @api_view(['POST'])
# def api_home(request, *args, **kwargs):
#     fcm_id = request.data['fcm_id']
#     print(fcm_id if fcm_id else '21321321321')

#     return JsonResponse({"message": "Hi there, this is your Django API response!!"})

def student_details(request,pk):
     #stu = Students.objects.get(id = pk)
    stu = Students.objects.filter(id = pk).first()
    serialize = StudentsSerializers(stu)
    #json_data = JSONRenderer().render(serialize.data)
    #return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serialize.data,safe= True)

    
def all_student(request):
    stu = Students.objects.all()
    serialize = StudentsSerializers(stu,many = True)
    json_data = JSONRenderer().render(serialize.data)
    return HttpResponse(json_data, content_type = 'application/json')


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentsSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def student_api(request):
    if request.method == 'POST':
        json_data = request.body
        if not json_data == b'':
            stream = io.BytesIO(json_data)
            pythonData = JSONParser().parse(stream)
            id = pythonData.get('id',None)
            if id is not None:
               stu = Students.objects.get(id = id)
               serializer = StudentsSerializers(stu)
               json_data = JSONRenderer().render(serializer.data)
               return HttpResponse(json_data,content_type = 'application/json')
            else:
                serializer = StudentsSerializers(data= pythonData)
                if serializer.is_valid():
                    serializer.save()
                    res = {'msg': 'Data Created'}
                    json_data = JSONRenderer().render(res)
                    return HttpResponse(json_data,content_type='application/json')
                else:
                    json_data = JSONRenderer().render(serializer.errors)
                    return HttpResponse(json_data,content_type='application/json')
                
        
        stu = Students.objects.all().values()
        serializer = StudentsSerializers(stu,many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = 'application/json')
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id',None)
        if id is not None:
            stu = Students.objects.get(id = id)
            serializer = StudentsSerializers(stu,data=pythonData,partial = True)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data updated'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')




    

        



        
        




