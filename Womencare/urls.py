
from django.contrib import admin
from django.urls import path

from Womencare.views import *

urlpatterns = [
#/////////////////////////////// ADMIN //////////////////////////////////

    path('', Login_Page.as_view(), name='LoginPage'),
    path('Admin_home',Admin_home.as_view(), name='Admin_home'),
    path('PoliceaddPage',PoliceaddPage.as_view(), name='PoliceaddPage'),
    path('CollegePage', CollegePage.as_view(), name='CollegePage'),
    path('CounsellorPage', CounsellorPage.as_view(), name='CounsellorPage'),
    path('EmergencyPage', EmergencyPage.as_view(), name='EmergencyPage'),
    path('lawyerPage', lawyerPage.as_view(), name='lawyerPage'),
    path('PolicePage', PolicePage.as_view(), name='PolicePage'),
    path('TeacherPage', TeacherPage.as_view(), name='TeacherPage'),
    path('userPage', userPage.as_view(), name='userPage'),
    path('AddCollegePage', AddCollegePage.as_view(), name='AddCollegePage'),
    path('DeleteCollege/<int:id>', DeleteCollege.as_view(), name='DeleteCollege'),
    path('AcceptCounsellor/<int:id>', AcceptCounsellor.as_view(),name='AcceptCounsellor'),
    path('RejectCounsellor/<int:id>', RejectCounsellor.as_view(),name='RejectCounsellor'),
    

# //////////////////////////////// cousellor///////////////////////////////

   path('CounsellorRegisterPage', CounsellorRegisterPage.as_view(), name='CounsellorRegisterPage'),
   path('MentalHealthSupportPage', MentalHealthSupportPage.as_view(), name='MentalHealthSupportPage'),

   # //////////////////////////////// Api///////////////////////////////

   path('UserReg',UserReg.as_view(),name='UserReg'),
   path('TeacherReg',TeacherReg.as_view(),name='TeacherReg'),
   path('ViewColleges',ViewColleges.as_view(),name='ViewColleges'),

]
