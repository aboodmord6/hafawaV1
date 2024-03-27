from django import forms
from .models import MyUser



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "w-full rounded-lg border-none bg-main1 shadow-inner p-3 text-lg"}) )
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={"class": "w-full rounded-lg border-none bg-main1 shadow-inner p-3 text-lg"}) )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    class Meta:
        model = MyUser
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "w-full rounded-lg border-none bg-main1 shadow-inner p-3 text-lg"})
        }

    def save(self, commit=True):
        user = super().save()
        user.set_password(self.cleaned_data["password1"])
        user.is_admin = False
        user.is_visitor = True
        user.save()
        return user