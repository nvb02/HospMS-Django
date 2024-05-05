from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 1. USER AUTHENTICATION AND ACCESS CONTROL::
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=300,default='username')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    


# 2. PATIENT MANAGEMENT::
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')])
    contact_number = models.IntegerField()
    medical_history = models.TextField(blank=True)
    address = models.CharField(max_length=200)
    
    
# 3. DOCTOR AND STAFF MANAGEMENT::
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    contact_no = models.IntegerField()

class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ManyToManyField(Doctor)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=[('Scheduled', 'scheduled'), ('Completed', 'completed'), ('Cancelled', 'cancelled')])

    
    
 
# 4. APPOINTMENT MANAGEMENT::    
class AppointmentRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    requested_date = models.DateField()
    requested_time = models.TimeField()
    reason = models.TextField()


    
# 5. MEDICAL RECORDS MANAGEMENT::
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    treated_by = models.ManyToManyField(Doctor)
    
    
# 6. BILLING AND PAYMENT::
class PatientConsultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    doctor_fee = models.FloatField()
    notes = models.TextField()
    
class Procedure(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    cost = models.FloatField()
    date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    process = models.TextField(null=True, blank=True)
    
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    issue_date = models.DateField()
    total_amount = models.FloatField()
    consultations = models.ManyToManyField(PatientConsultation)
    procedures = models.ManyToManyField(Procedure)
    
    

# 7. INVENTORY MANAGEMENT::
class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit_price = models.FloatField()
    category = models.CharField(max_length=100)  # E.g., 'Medical Supplies', 'Equipment', 'Medications'

class InventoryUsage(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity_used = models.PositiveIntegerField()
    used_by = models.CharField(max_length=100)  # E.g., Patient ID, Department Name
    usage_date = models.DateField(auto_now_add=True)
    
class InventoryExpense(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    expense_amount = models.FloatField()
    expense_type = models.CharField(max_length=100)  # E.g., 'Purchase', 'Maintenance'
    expense_date = models.DateField()


# 8. REPORTS AND ANALYTICS::
class RevenueExpense(models.Model):
    category = models.CharField(max_length=100) # eg - consultation fees, medication costs, equipment purchases etc..
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField()

class Report(models.Model):
    REPORT_CHOICES = [
        ('patient_demographics', 'Patient Demographics'),
        ('appointment_summary', 'Appointment Summary'),
        ('revenue', 'Revenue Report'),
        ('expenses', 'Expenses Report')
    ]
    report_type = models.CharField(max_length=50, choices=REPORT_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()



# 9. EMERGENCY MANAGEMENT:
class EmergencySituation(models.Model):
    emergency_type = models.CharField(max_length=300)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    triage_status = models.CharField(max_length=20, choices=[('Critical', 'critical'), ('Urgent', 'urgent'), ('Stable', 'stable')])
    arrival_time = models.DateTimeField(auto_now_add=True)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField()





