
from django import forms
from .models import PR_profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = PR_profile
        fields = '__all__'
