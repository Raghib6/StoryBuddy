from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mptt.forms import TreeNodeChoiceField
from .models import Story
class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(UserSignUpForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Password does not match !')

class StoryForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Story.objects.all(), required=False)

    class Meta:
        model = Story
        fields = ['parent','title','details']

    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter title of your story'
        self.fields['details'].widget.attrs['placeholder'] = 'Write your story here'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'