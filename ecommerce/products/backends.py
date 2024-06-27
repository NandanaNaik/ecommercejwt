from django.contrib.auth.backends import ModelBackend
from products.models import UserDetails

class EmployeeBackend(ModelBackend):
    def authenticate(self, request, emp_name=None, password=None, **kwargs):
        try:
            user = UserDetails.objects.get(emp_name=emp_name)
            if user.password == password:
                return user
        except UserDetails.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserDetails.objects.get(pk=user_id)
        except UserDetails.DoesNotExist:
            return None
