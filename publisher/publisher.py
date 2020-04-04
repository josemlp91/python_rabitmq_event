from kombu import Connection, Exchange
from yosun import Yosun
from datetime import datetime
import uuid

import time
import random
import string
import os

from common import Animal, AnimalEventData, AnimalEvent

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASS = os.getenv('RABBITMQ_PASS')


def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


AMQP_URL = 'amqp://{0}:{1}@{2}:{3}'.format(RABBITMQ_USER, RABBITMQ_PASS, RABBITMQ_HOST, RABBITMQ_PORT)

# Define Connection
connection = Connection(AMQP_URL)

# RabbitMQ Exchange definition
exchange = Exchange('events', type='topic')

# Yosun initialize
yosun = Yosun(connection, exchange)


if __name__ == "__main__":
    while True:

        animal = Animal(name=random_string())
        animal_event_data = AnimalEventData(
            id=uuid.uuid1(), type="domain_event_name", ocurred_on=datetime.now(), attributes=animal
        )

        animal_event = AnimalEvent(data=animal_event_data)

        yosun.publish('animals.rabbit', animal_event.dict())
        time.sleep(10)
