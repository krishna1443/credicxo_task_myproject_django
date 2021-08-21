from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Teacher, Student
from .serializers import TeacherSerializer, StudentSerializer

from django.contrib.auth.decorators import login_required




def login_message(request):
    return JsonResponse({"message":"Please Login First!!!"})

@login_required(login_url='/easytuts/login_message/')
@csrf_exempt
def student_details(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    #GET http://127.0.0.1:8000/student_details/1
    # get student details by id
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
    return HttpResponse(status=404)

@login_required(login_url='/easytuts/login_message/')
@csrf_exempt
def students(request):
    # List of Students, GET http://127.0.0.1:8000/easytuts/students/
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    # Add Student, POST http://127.0.0.1:8000/easytuts/students/
    # Body raw JSON(application/json)
    #
        # {
        #     "first_name": "python",
        # "last_name": "django",
        # "email": "python@g.com",
        # "address": "nowherer"

        # }
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
 
@login_required(login_url='/easytuts/login_message/')
@csrf_exempt
def teachers(request):
    # List of  Teachers, GET http://127.0.0.1:8000/easytuts/teachers/
    if request.method == 'GET':
        teachers =  Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse(serializer.data, safe=False)

    # Add  Teacher, POST http://127.0.0.1:8000/easytuts/teachers/
    # Body raw JSON(application/json)
    #
    # {
    #    "first_name":"pooja",
    #    "last_name" : "patil",
	#    "email" :"pooja@g.com" ,
	#    "address" : "rau",
	#    "position":"INSTRUCTOR"
    #  }
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =  TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
 

 # login http://127.0.0.1:8000/api/token/
 # {
 #  "username":"admin",
 #  "password":"admin@123"
 # }