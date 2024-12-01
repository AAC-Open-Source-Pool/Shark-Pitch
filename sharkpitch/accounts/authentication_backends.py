from django.contrib.auth.backends import BaseBackend
from accounts.models import Signin

class EmailBackend(BaseBackend):
    """
    Custom authentication backend to authenticate using email and password.
    """
    def authenticate(self, request, email=None, password=None):
        try:
            user = Signin.objects.get(email=email)
            if user.password == password: 
                return user
        except Signin.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Signin.objects.get(pk=user_id)
        except Signin.DoesNotExist:
            return None