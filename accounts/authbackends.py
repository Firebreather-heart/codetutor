from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Student


class CustomUserModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print('auth start')
        UserModel = get_user_model()
        try:
            print('trying auth user model')
            user = UserModel.objects.get(username=username)
            if user.check_password(password):  # type: ignore
                print(user)
                return user
        except UserModel.DoesNotExist:
            try:
                print('trying student user model')
                student = Student.objects.get(username=username)
                print(student, 'student')
                if student.check_password(password):  # type: ignore
                    print(student, 'student')
                    return student
            except Exception as e:
                print(e)
            except Student.DoesNotExist:
                return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            try:
                return Student.objects.get(id=user_id)
            except Student.DoesNotExist:
                return None
