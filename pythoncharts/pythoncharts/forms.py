from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    fullname = forms.CharField(max_length = 10, required=True)

    username = forms.CharField(max_length = 10)
    #fullname = forms.CharField(max_length = 150)
    first_name = forms.CharField(max_length = 150)
    last_name = forms.CharField(max_length = 150)
    email = forms.EmailField()
    #empid = forms.DateField(widget = forms.SelectDateWidget)
    #empid  = forms.CharField(max_length = 11)
    #appdate = forms.DateField(widget = forms.SelectDateWidget)   
    #station = forms.CharField(max_length = 3) 

    class Meta:
        model = User
        fields = ('fullname', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        """, 'empid', 'appdate', 'station', 'password1', 'password2')"""