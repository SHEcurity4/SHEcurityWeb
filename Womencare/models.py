from email.headerregistry import Address
from django.db import models

# Create your models here.
class LoginTable(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Status=models.CharField(max_length=100,null=True,blank=True)

class CollegeTable(models.Model):
    login_id=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    College_name=models.CharField(max_length=100,null=True,blank=True)
    Phone_Number=models.BigIntegerField(null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=1500,null=True,blank=True)

class UserTable(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Phone_number=models.BigIntegerField()
    Email=models.CharField(max_length=100,null=True,blank=True)
    Gender=models.CharField(max_length=15,null=True,blank=True)
    Age=models.IntegerField()
    College_id=models.ForeignKey(CollegeTable,on_delete=models.CASCADE,null=True,blank=True)
    login_id=models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True,blank=True)
class ComplaintTable(models.Model):
    login_id = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True)
    complaint_type = models.CharField(max_length=50, default="general")
    Complaints = models.CharField(max_length=1500, null=True, blank=True)
    Reply = models.CharField(max_length=1500, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.login_id} - {self.complaint_type}"


class PoliceTable(models.Model):
    login_id=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    Phone_number=models.BigIntegerField()
    Email=models.CharField(max_length=100,null=True,blank=True)
    Gender=models.CharField(max_length=15,null=True,blank=True)
    post=models.CharField(max_length=100,null=True,blank=True)
    Stationaddress=models.CharField(max_length=1000,null=True,blank=True)

class EmergencyTable(models.Model):
    USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    Phone_number=models.BigIntegerField()

class LocationTable(models.Model):
    login_id=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    latitude=models.CharField(max_length=50,null=True,blank=True)
    longitude=models.CharField(max_length=50,null=True,blank=True)

class LawyerTable(models.Model):
    login_id=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    Phone_number=models.BigIntegerField()
    Email=models.CharField(max_length=100,null=True,blank=True)
    Gender=models.CharField(max_length=15,null=True,blank=True)
    Qualification=models.CharField(max_length=100,null=True,blank=True)

class TeacherTable(models.Model):
    login_id=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    College_id=models.ForeignKey(CollegeTable,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    Phone_number=models.BigIntegerField(max_length=20,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Gender=models.CharField(max_length=15,null=True,blank=True)
    Qualification=models.CharField(max_length=100,null=True,blank=True)

class FeedbackTable(models.Model):
    login_id=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    feedback=models.CharField(max_length=1000,null=True,blank=True)
    rating=models.IntegerField()
    date=models.DateField(auto_now_add=True)

class CounsellorTable(models.Model):
    login_id=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    Phone_number=models.BigIntegerField()
    Email=models.CharField(max_length=100,null=True,blank=True)
    Gender=models.CharField(max_length=15,null=True,blank=True)
    Qualification=models.CharField(max_length=100,null=True,blank=True)

class MentalHealthSupportTable(models.Model):
    login_id=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    Counsellor_id=models.ForeignKey(CounsellorTable,on_delete=models.CASCADE,null=True,blank=True)
    reason=models.CharField(max_length=1000,null=True,blank=True)
    reply=models.CharField(max_length=1000,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    


    








