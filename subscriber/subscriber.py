from kombu import Connection, Exchange
from yosun import Yosun
import os

from common import AnimalEvent

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASS = os.getenv('RABBITMQ_PASS')


AMQP_URL = 'amqp://{0}:{1}@{2}:{3}'.format(RABBITMQ_USER, RABBITMQ_PASS, RABBITMQ_HOST, RABBITMQ_PORT)

# Define Connection
connection = Connection(AMQP_URL)

# RabbitMQ Exchange definition
exchange = Exchange('events', type='topic')

# Yosun init
yosun = Yosun(connection, exchange)


def on_rabbit(body, message):
    rabbit_event = AnimalEvent(**body)
    print('Look, a rabbit!')
    print(rabbit_event)


def on_animal(body, message):
    animal_event = AnimalEvent(**body)
    print('Look, an animal!')
    print(animal_event)


sub = yosun.subscribe('animals.#')

# from now on when a animals.rabbit message arrives, on_rabbit will be called
sub.on('animals.rabbit', on_rabbit)

# when any message matching animals.# arrives, on_animal will be called
sub.all(on_animal)
