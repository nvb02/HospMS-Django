from django.urls import path
from .views import *

urlpatterns = [
    path('patient/', PatientView.as_view({'get':'list','post':'create'})),
    path('doctor/', DoctorView.as_view({'get':'list','post':'create'})),
    path('staff/', StaffView.as_view({'get':'list','post':'create'})),
    path('appointmentrequest/', AppointmentRequestView.as_view({'get':'list','post':'create'})),
    path('appointment/', AppointmentView.as_view({'get':'list','post':'create'})),
    path('medicalrecord/', MedicalRecordView.as_view({'get':'list','post':'create'})),
    path('patientconsultation/', PatientConsultationView.as_view({'get':'list','post':'create'})),
    path('procedure/', ProcedureView.as_view({'get':'list','post':'create'})),
    path('invoice/', InvoiceView.as_view({'get':'list','post':'create'})),
    path('inventoryitem/', InventoryItemView.as_view({'get':'list','post':'create'})),
    path('inventoryusage/', InventoryUsageView.as_view({'get':'list','post':'create'})),
    path('inventoryexpense/', InventoryExpenseView.as_view({'get':'list','post':'create'})),
    path('emergency/', EmergencyView.as_view({'get':'list','post':'create'})),
    path('revenueexpense/', RevenueExpenseView.as_view({'get':'list','post':'create'})),
    path('report/', ReportView.as_view({'get':'list','post':'create'})),
    
    path('patient/<int:pk>/', PatientView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('doctor/<int:pk>/', DoctorView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('staff/<int:pk>/', StaffView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('appointmentrequest/<int:pk>/', AppointmentRequestView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('appointment/<int:pk>/', AppointmentView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('medicalrecord/<int:pk>/', MedicalRecordView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('patientconsultation/<int:pk>/', PatientConsultationView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('procedure/<int:pk>/', ProcedureView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('invoice/<int:pk>/', InvoiceView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('inventoryitem/<int:pk>/', InventoryItemView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('inventoryusage/<int:pk>/', InventoryUsageView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('inventoryexpense/<int:pk>/', InventoryExpenseView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('emergency/<int:pk>/', EmergencyView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('revenueexpense/<int:pk>/', RevenueExpenseView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('report/<int:pk>/', ReportView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    
    path('login/',login),
    path('register/',register),
    path('role/',group_listing),
    path('logout/',logout)
]