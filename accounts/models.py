from django.db import models
from django.contrib.auth.models import User


def upload_to(instance, filename):
	return '%s/%s/%s' % ('profile_photo', instance.user.username, filename)


class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE, verbose_name='User')
	profile_photo = models.ImageField(upload_to=upload_to, default='profile_photo/avatar.jpg', verbose_name='Profile Photo')

	def __str__(self):
		return '%s Profile' % self.user.get_full_name

	class Meta:
		verbose_name_plural = "Users"
		verbose_name = "User"
