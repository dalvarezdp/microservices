# -*- coding: utf-8 -*-
import json
import pika

from django.core.management import BaseCommand
from django.conf import settings
from django.utils.encoding import smart_text


class Command(BaseCommand):

    help = "Runs an events subscriber"

    def callback(self, ch, method, properties, body):
        try:
            event = json.loads(smart_text(body))
        except Exception as error:
            self.stderr.write("Error: {0}".format(error))
        else:
            self.stdout.write("Event {0} received from {1}".format(event.get("type"), event.get("source")))
            self.stdout.write(json.dumps(event))
            # TODO: meter el código para enviar los e-mails al resto de usuarios

    def handle(self, *args, **options):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.MESSAGE_BUS.get("HOST")))
        channel = connection.channel()

        channel.exchange_declare(exchange=settings.MESSAGE_BUS.get("EXCHANGE"), type=settings.MESSAGE_BUS.get("TYPE"))

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange=settings.MESSAGE_BUS.get("EXCHANGE"), queue=queue_name)

        self.stdout.write(' [*] Waiting for logs. To exit press CTRL+C')

        channel.basic_consume(self.callback, queue=queue_name, no_ack=True)

        channel.start_consuming()
