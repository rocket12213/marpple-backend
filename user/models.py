from django.db import models

class SocialPlatform(models.Model):
    platform_name = models.CharField(max_length=20, unique = True)

    class Meta:
        db_table = 'social_platforms'

class User(models.Model):
    name               = models.CharField(max_length = 100, blank = True, null = True)
    email              = models.CharField(max_length = 200, unique = True, null = True)
    platform_id        = models.CharField(max_length = 100)
    social_platform    = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users'
