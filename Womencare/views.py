from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from rest_framework import status

from Womencare.serializer import BookingHsSerializer, BookingSerializer, CollegeSerializer, CounsellorSerializer, EmergencySerializer, LoginSerializer, MentalHealthSupportSerializer, TeacherSerializer, UserSerializer
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
        
        t_user = LoginTable.objects.filter(Username=username).first()
        print("$$$$$$$$$$$",t_user)
        
        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_401_UNAUTHORIZED)
        
        else:
            response_dict["message"] = "success"
            response_dict["login_id"] = t_user.id
            response_dict["usertype"] = t_user.Status

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
        
class AddEmergencyContact(APIView):
        def post(self,request,lid):
            print("==============", request.data)
            try:
                userid= UserTable.objects.get(login_id__id=lid)
            except UserTable.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            
            cont= EmergencySerializer(data=request.data)
            if cont.is_valid():
                cont.save(USERID=userid)
                return Response(cont.data, status=HTTP_200_OK)
            else:
                return Response(cont.errors, status=HTTP_400_BAD_REQUEST)

        def delete(self,request,lid):
            try:
                c=EmergencyTable.objects.get(id=lid)
                c.delete()
                return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
            except EmergencyTable.DoesNotExist:
                return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)
                
        def get(self,request,lid):
                c=EmergencyTable.objects.filter(USERID__login_id__id=lid)
                ser=EmergencySerializer(c, many=True)
                return Response( ser.data, status=status.HTTP_200_OK)    
    

class ViewCounc(APIView):
    def get(self, request):
        c = CounsellorTable.objects.filter(login_id__Status = "Counsellor")
        ser = CounsellorSerializer(c, many=True)
        return Response(ser.data, status=HTTP_200_OK)
  

class BookCounsellor(APIView):
    def post(self, request, lid):
        print(request.data)
        c = UserTable.objects.get(login_id__id = lid)
        ser = BookingSerializer(data=request.data)
        if ser.is_valid():
            ser.save(login_id=c ,status="pending")
            return Response(ser.data, status=HTTP_200_OK) 
        else:
            return Response(ser.errors, status=HTTP_400_BAD_REQUEST)
        
    def get(self,request,lid):
        c = MentalHealthSupportTable.objects.filter(login_id__login_id__id = lid) 
        ser = BookingHsSerializer(c, many=True)
        return Response(ser.data, status=HTTP_200_OK) 

# class GetALLMobileNumbers(APIView):
#     def get(self, request, lid):
#         emergency  