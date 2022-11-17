from django.shortcuts import render
from .serializer import StudentRegisterationSerializer, AppointmentScheduleSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import StudentRegisteration
from .models import AppointmentSchedule
from django.utils import timezone


class StudentList(APIView):
    
    def get(self, request, format=None):
        try:
            students = StudentRegisteration.objects.all()
            serializer = StudentRegisterationSerializer(students, many=True)
            res = {"status_code": 200, "data": serializer.data, "message": "Success"}
            return Response(res, status=status.HTTP_200_OK)
        
        except Exception as e:
            res = {"status_code": 500, "message": str(e)}
            return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentApi(APIView):


    def get_object(self, pk):
        try:
            return StudentRegisteration.objects.get(pk=pk)
        
        except StudentRegisteration.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):

        try: 
            students = self.get_object(pk)
            serializer = StudentRegisterationSerializer(students)
            res = {"status_code": 200, "data": serializer.data, "message": "Success"}
            return Response(res, status=status.HTTP_200_OK)
        
        except Exception as e:
            res = {"status_code": 500, "message": str(e)}
            return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def post(self, request, format=None):
        try: 
            serializer = StudentRegisterationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                res = {"status_code": 200, "data": serializer.data, "message": "Success"}
                return Response(res, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            res = {"status_code": 500, "message": str(e)}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk, format=None):
        try:
            student = self.get_object(pk)
            serializer = StudentRegisterationSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                res = {"status_code": 200, "data": serializer.data, "message": "Success"}
                Response(res, status=status.HTTP_200_OK)
            
        except Exception as e:
                res = {"status_code": 500, "message": str(e)}
                return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk, format=None):
        try:
            student = self.get_object(pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
                res = {"status_code": 500, "message": str(e)}
                return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
     
# task -- create event upcoming and due event api  
class EventApi(APIView):
    
    serializer = AppointmentScheduleSerializer
    
    def get(self, request):
        try:
            now = timezone.now()
            params = self.request.query_params
            event_type = params.get('event_type')

            if event_type == "upcoming":
                upcoming_appointment = AppointmentSchedule.objects.filter(appointment_date__gt=now).order_by(
                    'appointment_date')
                serializer = self.serializer(upcoming_appointment, many=True)
                res = {"status_code": 200, "data": serializer.data, "message": "Success"}
                return Response(res, status=status.HTTP_200_OK)

            elif event_type == "due":
                due_appointment = AppointmentSchedule.objects.filter(appointment_date__lt=now).order_by(
                    '-Appointment_date')
                serializer = self.serializer(due_appointment, many=True)
                res = {"status_code": 200, "data": serializer.data, "message": "Success"}
                return Response(res, status=status.HTTP_200_OK)

            else:
                all_appointment = AppointmentSchedule.objects.all()
                serializer = self.serializer(all_appointment, many=True)
                res = {"status_code": 200, "data": serializer.data, "message": "Success"}
                return Response(res, status=status.HTTP_200_OK)

        except Exception as e:
            res = {"status_code": 500, "message": str(e)}
            return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
        
        