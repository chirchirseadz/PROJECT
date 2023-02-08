from django import forms
from .models import Message
from users.models import CustomUser


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['your_name', 'email', 'subject', 'message']

class AdminUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['password', 'username', 'first_name', 'last_name', 'email', 'is_active']
        # fields = "__all__"


