from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from rest_framework import status

from Womencare.serializer import CollegeSerializer, LoginSerializer, TeacherSerializer, UserSerializer
from Womencare.models import *

# Create your views here.
class Admin_home(View):
    def get(self,request):
        return render(request, 'administration/home.html')
    

class Login_Page(View):
    def get(self, request):
        return render(request, 'administration/login.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        try:
            obj = LoginTable.objects.get(Username=username,Password=password)
            request.session['user_id'] = obj.id

            # Handle based on user type
            if obj.Status=='admin':
                return HttpResponse('''<script>alert("Wlcome back");window.location='/Admin_home'</script>''')
            else:
                return HttpResponse('''<script>alert("User not found");window.location='/'</script>''')
        except LoginTable.DoesNotExist:
            # Handle case where login details do not exist   
            return HttpResponse('''<script>alert("Invalid username or password");window.location='/'</script>''')
        class Classroom(View):
            def get(self,request):
                return render(request,"administration/classroom.html")
       
    
 # /////////////////////////// ADMIN ////////////////////////////////////

class PoliceaddPage(View):
    def get(self, request):
        return render(request, 'administration/policeadd.html')
    
class CollegePage(View):
    def get(self, request):
        obj = CollegeTable.objects.all()
        return render(request, 'administration/viewcollege.html', {'val': obj})

class CounsellorPage(View):
    def get(self, request):
        obj=CounsellorTable.objects.all()
        return render(request, 'administration/viewcounsellor.html',{'val':obj})
class EmergencyPage(View):
    def get(self, request):
        obj=EmergencyTable.objects.all()
        return render(request, 'administration/viewemergency.html',{'val':obj})
class lawyerPage(View):
    def get(self, request):
        obj=LawyerTable.objects.all()
        return render(request, 'administration/viewlawyer.html',{'val':obj})
class PolicePage(View):
    def get(self, request):
        obj=PoliceTable.objects.all()
        return render(request, 'administration/viewpolice.html',{'val':obj})
class TeacherPage(View):
    def get(self, request):
        obj=TeacherTable.objects.all()
        return render(request, 'administration/viewteacher.html',{'val':obj})
class userPage(View):
    def get(self, request):
        obj=UserTable.objects.all()
        return render(request, 'administration/viewuser.html',{'val':obj})
class AddCollegePage(View):
    def get(self, request):
        return render(request, 'administration/addcollege.html')
    
# /////////////////////////////////   ///////////////////////////////////////
    
class CounsellorRegisterPage(View):
    def get(self, request):
        return render(request, 'administration/councereg.html')
class MentalHealthSupportPage(View):
    def get(self, request):
        return render(request, 'administration/mentalhealthsupport.html')   
class DeleteCollege(View):
    def get(self,request,id):
        c=CollegeTable.objects.get(id=id)
        c.delete()
        return redirect('/CollegePage')
    
class AcceptCounsellor(View):
    def get(self,request,id):
        c=CounsellorTable.objects.get(id=id)
        c.login_id.Status='Counsellor'
        c.login_id.save()
        return HttpResponse('''<script>alert('Counsellor is verified successfully!');window.location='/CounsellorPage'</script>''')
class RejectCounsellor(View):
    def get(self,request,id):
        c=CounsellorTable.objects.get(id=id)
        c.login_id.Status='Rejected'
        c.login_id.save()
        return HttpResponse('''<script>alert('Counsellor Rejected successfully!');window.location='/CounsellorPage'</script>''')
    





# //////////////////////////////////////////////////  API  //////////////////////////////

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED
)

class LoginPage(APIView):
    def post(self, request):
        print("#####################")
        response_dict = {}

        username = request.data.get("username")
        password = request.data.get("password")
        print("$$$$$$$$$$$$$$",username)

        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_400_BAD_REQUEST)
        
        t_user = LoginTable.objects.filter(username=username).first()
        print("$$$$$$$$$$$",t_user)
        
        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_401_UNAUTHORIZED)
        
        else:
            response_dict["message"] = "success"
            response_dict["login_id"] = t_user.id

            return Response(response_dict, status=HTTP_200_OK)

class UserReg(APIView):
    def post(self,request):
        print("###################", request.data)

        user_serial = UserSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)

        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            login_profile = login_serial.save(Status='USER')

            user_serial.save(login_id=login_profile)

            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        
        return Response({
            'login_error': login_serial.errors if not login_valid else None,
            'user_error': user_serial.errors if not data_valid else None
            },status=status.HTTP_400_BAD_REQUEST) 
        

class ViewColleges(APIView):
    def get (self,request):
        c=CollegeTable.objects.all()
        serializer=CollegeSerializer(c,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class TeacherReg(APIView):
    def post(self,request):
        print("###################", request.data)

        teacher_Serializer = TeacherSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)

        data_valid = teacher_Serializer.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            login_profile = login_serial.save(Status='TEACHER')

            teacher_Serializer.save(login_id=login_profile)

            return Response(teacher_Serializer.data, status=status.HTTP_201_CREATED)
        
        return Response({
            'login_error': login_serial.errors if not login_valid else None,
            'teacher_error': teacher_Serializer.errors if not data_valid else None
            },status=status.HTTP_400_BAD_REQUEST)       
