from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'role', 'worker_type', 'membership_status', 'profile_picture', 'rating')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['worker_type'].required = False
        self.fields['rating'].required = False

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'role', 'worker_type', 'membership_status', 'profile_picture', 'rating')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['worker_type'].required = False
        self.fields['rating'].required = False
