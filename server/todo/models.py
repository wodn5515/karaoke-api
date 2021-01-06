from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import User
import datetime

# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey(User, verbose_name=_("회원"), on_delete=models.CASCADE)
    todo = models.CharField(_("할 일"), max_length=100, help_text=_("100자 이내로 입력해주세요."))
    date = models.DateTimeField(_("일시"), default=datetime.datetime.now())

    class Meta:
        verbose_name = "할 일"
        verbose_name_plural = "할 일"

    def __str__(self):
        return f"{self.todo}"
