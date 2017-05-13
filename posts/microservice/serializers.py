# -*- coding: utf-8 -*-
from rest_framework import serializers

from microservice.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
