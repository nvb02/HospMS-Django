from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

# Create your views here.

class PatientView(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    search_fields = ['name','age','gender']
    
class DoctorView(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class StaffView(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class AppointmentRequestView(ModelViewSet):
    queryset = AppointmentRequest.objects.all()
    serializer_class = AppointmentRequestSerializer

class AppointmentView(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MedicalRecordView(ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    filterset_fields = ['patient']
    search_fields = ['diagnosis','record_date']

class PatientConsultationView(ModelViewSet):
    queryset = PatientConsultation.objects.all()
    serializer_class = PatientConsultationSerializer

class ProcedureView(ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

class InvoiceView(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InventoryItemView(ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class InventoryUsageView(ModelViewSet):
    queryset = InventoryUsage.objects.all()
    serializer_class = InventoryUsageSerializer

class InventoryExpenseView(ModelViewSet):
    queryset = InventoryExpense.objects.all()
    serializer_class = InventoryExpenseSerializer

class RevenueExpenseView(ModelViewSet):
    queryset = RevenueExpense.objects.all()
    serializer_class = RevenueExpenseSerializer

class ReportView(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    
class EmergencyView(ModelViewSet):
    queryset = EmergencySituation.objects.all()
    serializer_class = EmergencySerializer
    
@api_view(['POST'])
@permission_classes([AllowAny,])
def register(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hash_password = make_password(password)
        a = serializer.save()
        a.password = hash_password
        a.save()
        return Response('User Created!')
    else:
        return Response(serializer.errors)   
    
    
@api_view(['POST'])
@permission_classes([AllowAny,])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email, password=password)
    if user == None:
        return Response('Email or password is incorrect!')
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    

@api_view(['GET'])
@permission_classes([AllowAny,])
def group_listing(request):
    group_objs = Group.objects.all()
    serializer = GroupSerializer(group_objs,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def logout(request):
    request.user.auth_token.delete()
    logout(request._request)
    return Response("Logged out successfully")
