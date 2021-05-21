

import pika, json

params = pika.URLParameters('amqps://epkkwwwl:4CN0Sg0ztKcS7MWBSK2X-J7LOCAs7hDL@puffin.rmq2.cloudamqp.com/epkkwwwl')


connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method,body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin',body=json.dumps(body),properties=properties)