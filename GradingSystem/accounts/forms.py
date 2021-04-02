from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()


from .models import smisformsdb

class smis_register(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(smis_register, self).__init__(*args, **kwargs)
        self.fields['username'].empty_label = '--Enter Your Reg No--'


class smis_forms(forms.ModelForm):

    class Meta:
        model = smisformsdb
        fields = ('student_name', 'registration_no', 'course','marks')
        labels = {
            'student_name': ' ',
            'registration_no': ' ',
            'course': ' ',
            'marks': ' '
        }

    def __init__(self, *args, **kwargs):
        super(smis_forms, self).__init__(*args, **kwargs)
        self.fields['registration_no'].default='username'
