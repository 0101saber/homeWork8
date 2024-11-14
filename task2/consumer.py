import pika
from conf.models import Contact
from bson import ObjectId
import conf.connect

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue')


def send_email_stub(contact):
    print(f"Sending email to {contact.email}")
    return True


def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    contact = Contact.objects(id=ObjectId(contact_id)).first()

    if contact and not contact.sent:
        if send_email_stub(contact):
            contact.sent = True
            contact.save()
            print(f"Email sent to {contact.fullname}.")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='email_queue', on_message_callback=callback)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
