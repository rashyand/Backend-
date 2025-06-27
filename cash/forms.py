from django import forms
from django.contrib.auth.models import User
from .models import Item 
 

# User registration form
class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.set_password(self.cleaned_data["password"])  # Set the password securely
            user.save()
        return user



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item 
        fields = ['name', 'category', 'description', 'quantity', 'price']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'