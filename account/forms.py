from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm  
class FormUser(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(FormUser,self).__init__(*args, **kwargs)
        self.fields["username"].disabled = True
        self.fields["email"].disabled = True
        self.fields["special_suer"].disabled = True
    class Meta():
        model = User
        fields = ["username", "email","first_name","last_name", "address","special_suer"]


class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='اجباری')  
    class Meta:  
        model = User  
        fields = ['username','email', ] 