
from django.contrib import admin
from django.urls import path

from Womencare.views import *

urlpatterns = [
#/////////////////////////////// ADMIN //////////////////////////////////

    path('', Login_Page.as_view(), name='LoginPage'),
    path('Admin_home',Admin_home.as_view(), name='Admin_home'),
    path('PoliceaddPage',PoliceaddPage.as_view(), name='PoliceaddPage'),
    path('CollegePage', CollegePage.as_view(), name='CollegePage'),
    path('viewcounsellor', CounsellorPage.as_view(), name='viewcounsellor'),
    path('viewemergency', EmergencyPage.as_view(), name='viewemergency'),
    path('viewlawyer', lawyerPage.as_view(), name='viewlawyer'),
    path('viewpolice', PolicePage.as_view(), name='viewpolice'),
    path('viewteacher', TeacherPage.as_view(), name='viewteacher'),
    path('viewuser', userPage.as_view(), name='viewuser'),
    path('AddCollegePage', AddCollegePage.as_view(), name='AddCollegePage'),
    path('DeleteCollege/<int:id>', DeleteCollege.as_view(), name='DeleteCollege'),
    path('AcceptCounsellor/<int:id>', AcceptCounsellor.as_view(),name='AcceptCounsellor'),
    path('RejectCounsellor/<int:id>', RejectCounsellor.as_view(),name='RejectCounsellor'),
    path('AcceptLawyer/<int:id>', AcceptLawyer.as_view(),name='AcceptLawyer'),
    path('RejectLawyer/<int:id>', RejectLawyer.as_view(),name='RejectLawyer'),
    path('AcceptTeacher/<int:id>', AcceptTeacher.as_view(),name='AcceptTeacher'),
    path('RejectTeacher/<int:id>', RejectTeacher.as_view(),name='RejectTeacher'),
    path('DeletePolice/<int:id>', DeletePolice.as_view(), name='DeletePolice'),

    

# //////////////////////////////// cousellor///////////////////////////////

   path('CounsellorRegisterPage', CounsellorRegisterPage.as_view(), name='CounsellorRegisterPage'),
   path('mentalhealthsupport', MentalHealthSupportPage.as_view(), name='mentalhealthsupport'),
  


   # //////////////////////////////// Api///////////////////////////////

   path('UserReg',UserReg.as_view(),name='UserReg'),
   path('LoginPage',LoginPage.as_view(),name='LoginPage'),
   path('TeacherReg',TeacherReg.as_view(),name='TeacherReg'),
   path('ViewColleges',ViewColleges.as_view(),name='ViewColleges'),
   path('EmergencyContacts/<int:lid>',AddEmergencyContact.as_view(),name='AddEmergencyContact'),
   path('viewcounsellors',ViewCounc.as_view(),name='viewcounsellors'),
   path('BookCounsellor/<int:lid>',BookCounsellor.as_view(),name='BookCounsellor'),
   path('GetAllNumbers/<int:lid>',GetAllMobileNumbers.as_view(),name='GetAllNumbers'),
   path('add_complaint/', AddComplaint.as_view()),
   path('get_complaints/<int:login_id>/', GetComplaints.as_view()), 
   path('Lawyerregister',Lawyerregister.as_view(),name='Lawyerregister'),       

    path('complaints/', ComplaintAPIView.as_view(), name='complaints-api'),
    path('complaintsteacher/', ComplaintTeacherAPIView.as_view(), name='complaintsteacher'),
    path('feed/<int:id>', Feedbackapi.as_view())
]   
