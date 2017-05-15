# -*- coding: utf-8 -*-
import pika
import json
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from microservice.models import Post
from microservice.serializers import PostSerializer


class PostViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()

        event = {
            "source": "posts-microservice",
            "type": "post-created",
            "data": serializer.data
        }

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='events', type='fanout')
        channel.basic_publish(exchange='events', routing_key='', body=json.dumps(event))
        connection.close()
