# -*- coding: utf-8 -*-
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from microservice.models import Post
from microservice.serializers import PostSerializer


class PostViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
