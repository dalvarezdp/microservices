# -*- coding: utf-8 -*-
from django.db import models


class Post(models.Model):

    user_id = models.IntegerField()     # id del autor del post
    image = models.FileField()
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
