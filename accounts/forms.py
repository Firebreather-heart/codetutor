from django import forms
from .models import Student, School, ClassRoom


class StudentForm(forms.ModelForm):
    school = forms.ModelChoiceField(queryset=School.objects.all())
    classroom = forms.ModelChoiceField(queryset=ClassRoom.objects.all())

    class Meta:
        model = Student
        fields = ['username', 'email', 'school', 'classroom', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
