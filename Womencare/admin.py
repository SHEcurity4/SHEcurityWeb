from django.contrib import admin

from Womencare.models import CollegeTable, ComplaintTable, CounsellorTable, EmergencyTable, FeedbackTable, LawyerTable, LocationTable, LoginTable, MentalHealthSupportTable, PoliceTable, TeacherTable, UserTable

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(LocationTable)
admin.site.register(LawyerTable)
admin.site.register(FeedbackTable)
admin.site.register(EmergencyTable)
admin.site.register(CounsellorTable)
admin.site.register(ComplaintTable)
admin.site.register(CollegeTable)
admin.site.register(MentalHealthSupportTable)
admin.site.register(PoliceTable)
admin.site.register(TeacherTable)
admin.site.register(UserTable)


