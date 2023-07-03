from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
    # 항목하나마다 하나의 DB column
    title = models.CharField(max_length=50)
    content = models.TextField()

    # 다른 앱에 있는 모델 참조 (3가지)

    # 방법1. (권장하지 않음)
    # user = models.ForeignKey(User)

    # 방법2. (권장) settings.AUTH_USER_MODEL == 'accounts.User'
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 방법3. (권장)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)