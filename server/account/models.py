from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password):
        if not username:
            raise ValueError("아이디를 입력해주세요.")
        if not email:
            raise ValueError("이메일을 입력해주세요.")
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    username = models.CharField(_("ID"), max_length=20, unique=True)
    nickname = models.CharField(_("닉네임"), max_length=16, unique=True, null=True)
    is_staff = models.BooleanField(_("스태프"), default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "회원"
        verbose_name_plural = "회원"