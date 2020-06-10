from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.CharField(max_length=100)
    portfolio_site = models.CharField(max_length=100)
    def __str__(self):
      return self.user.username
    class Meta:
        db_table:'usertable'