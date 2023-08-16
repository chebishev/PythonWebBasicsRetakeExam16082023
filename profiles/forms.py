from django import forms

from profiles.models import ProfileModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'profile_picture', 'password']
        widgets = {
            'password': forms.PasswordInput
        }