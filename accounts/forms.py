from django import forms
from .models import Student, School, ClassRoom, CustomClassRoom


class StudentForm(forms.ModelForm):
    school = forms.ModelChoiceField(queryset=School.objects.all())
    classroom = forms.ModelChoiceField(queryset=ClassRoom.objects.all(), required=False)
    custom_classroom = forms.ModelChoiceField(queryset=CustomClassRoom.objects.all(), help_text='Select this if you are private student', label='Private Classroom', required=False )
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['username', 'email', 'school', 'classroom', 'custom_classroom',  'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
