from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import Profile

class custom_user_creation(UserCreationForm):
    class Meta:
        model = User
        fields =  ['first_name','email','username','password1','password2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].label = 'Password Again'
        self.fields['first_name'].label = 'Name'
    

class profile_form(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','location','bio','short_intro','profile_image']
