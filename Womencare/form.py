from django.forms import ModelForm
from Womencare.models import *


class PoliceForm(ModelForm):
    class Meta:
        model=PoliceTable
        fields="__all__"

class CouncellorForm(ModelForm):
    class Meta:
        model=CounsellorTable
        fields="__all__"
