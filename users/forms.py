from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.forms import (PasswordResetForm, UserChangeForm,
                                       UserCreationForm)
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)
    age_verification = forms.BooleanField(required=True)
    
    """ Add phone number field using thid party package PhoneNumberField"""

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

        for fieldname in ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ManageAccountForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
            super(UserChangeForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_show_labels = False 

            for fieldname in ['username', 'email']:
                self.fields[fieldname].help_text = None

    class Meta:
        model = User
        # ADD PHONE NUMBER
        fields = ('username', 'email')


