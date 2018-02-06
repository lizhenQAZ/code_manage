from db.abstractmodels import AbstaractModel
from django.db import models
from utils.wrappers import post, encrypt_password


class UserManager(models.Manager):
    def user_by_username(self, username):
        try:
            return self.get(user=username)
        except User.DoesNotExist:
            return None

    def save_user(self, request):
        user = User()
        user.user = post(request, 'user_name')
        user.pwd = encrypt_password(post(request, 'pwd'))
        user.email = post(request, 'email')
        user.save()


class User(AbstaractModel):
    user = models.CharField(max_length=30)
    pwd = models.CharField(max_length=70)
    email = models.CharField(max_length=50)
    objects = UserManager()
