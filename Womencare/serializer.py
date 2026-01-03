from rest_framework import serializers

from Womencare.models import *

class  LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model= LoginTable
        fields=['Username','Password']

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model= CollegeTable
        fields=['College_name','Phone_Number','Email','Address', 'id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserTable
        fields=['Name','Phone_number','Email','Gender','Age','College_id']

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = '__all__'


class PoliceSerializer(serializers.ModelSerializer):
    class Meta:
        model= PoliceTable
        fields=['login_id','Name','Phone_number','Email','Gender','post','Stationaddress']        

class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model= EmergencyTable
        fields='__all__'     

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model= LocationTable
        fields=['login_id','latitude','longitude']

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model= LawyerTable
        fields=['login_id','Name','Phone_number','Email','Gender','Qualification']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= TeacherTable
        fields=['College_id','Name','Phone_number','Email','Gender','Qualification']        

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model= FeedbackTable
        fields=['login_id','feedback','rating','date']            

class CounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model= CounsellorTable
        fields=['id','login_id','Name','Phone_number','Email','Gender','Qualification']       

class MentalHealthSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model= MentalHealthSupportTable
        fields=['login_id','Counsellor_id','reason','reply','date']       
class  BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model= MentalHealthSupportTable
        fields="__all__"  

class BookingHsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='Counsellor_id.Name')
    support_request_id = serializers.CharField(source='id')
    class Meta:
        model = MentalHealthSupportTable
        fields = ['status','date','name','reason','reply','support_request_id']        


class ComplaintsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='login_id.Username')
    class Meta:
        model = ComplaintTable
        fields = ['id','Complaints', 'username','Reply','date']


class Feedbackser(serializers.ModelSerializer):
    class Meta:
        model = FeedbackTable
        fields = '__all__'