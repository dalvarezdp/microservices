# -*- coding: utf-8 -*-
import json
import pika
from django.core.management import BaseCommand


class Command(BaseCommand):

    help = "Publish an event in the bus"

    def handle(self, *args, **options):

        event = {
            "source": "posts-microservice",
            "type": "post-created",
            "data": {
                "id": 12,
                "user_id": 11,
                "image": "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/11/yoda-the-empire-strikes-back.jpg",
                "description": "Yoda in Dagobah"
            }
        }

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='events', type='fanout')
        channel.basic_publish(exchange='events', routing_key='', body=json.dumps(event))
        self.stdout.write(" [x] Sent event")
        connection.close()
