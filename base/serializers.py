from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email','password','groups','username']       
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class AppointmentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentRequest
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

class PatientConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientConsultation
        fields = '__all__'

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class InventoryUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryUsage
        fields = '__all__'

class InventoryExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryExpense
        fields = '__all__'

class RevenueExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueExpense
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        
class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencySituation
        fields = '__all__'