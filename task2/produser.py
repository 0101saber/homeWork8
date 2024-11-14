import pika
from faker import Faker
from conf.models import Contact
import conf.connect

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

fake = Faker()


def generate_contacts(n=10):
    for _ in range(n):
        contact = Contact(
            fullname=fake.name(),
            email=fake.email()
        )
        contact.save()

        channel.basic_publish(
            exchange='',
            routing_key='email_queue',
            body=str(contact.id)
        )
        print(f"Contact {contact.fullname} added to queue with ObjectID {contact.id}")


generate_contacts(10)
connection.close()
