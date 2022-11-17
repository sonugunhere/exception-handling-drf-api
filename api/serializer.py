from accounts.models import StudentRegisteration,SchoolManagement
from rest_framework import serializers
from .models import AppointmentSchedule
from django.utils import timezone



class SchoolManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolManagement
        fields = ['id', 'user', 'username', 'school', 'email', 'contact', 'dise_code', 'address', 'city', 'state', 'country', 'school_type', 'password', 'confirm_password']



class StudentRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRegisteration
        fields = ['id', 'school', 'first_name', 'last_name', 'email', 'contact_no', 'father_name', 'mother_name', 'address', 'dob', 'standard', 'gender', 'batch', 'adhar_card']


# task -- create event upcoming and due event api      
class AppointmentScheduleSerializer(serializers.ModelSerializer):
    event_type = serializers.SerializerMethodField()
 
    class Meta:
        model = AppointmentSchedule
        fields = ("id", "customer_name", "appointment_date", "description", "event_type")
        
    def get_event_type(self, obj):
        
        if obj.appointment_date > timezone.now():
            return "UPCOMING"
        
        if obj.appointment_date < timezone.now():
            return "DUE"
        
        else:
            return "UNDEFINED"