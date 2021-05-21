import pika, json, os,django


os.environ.setdefault("DJANGO_SETTINGS_MODULE","admin.settings")
django.setup()


from products.models import Product


params = pika.URLParameters('amqps://epkkwwwl:4CN0Sg0ztKcS7MWBSK2X-J7LOCAs7hDL@puffin.rmq2.cloudamqp.com/epkkwwwl')


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue= 'admin')


def callback(ch, method, properties, body):
    print('received admin...')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes+1
    product.save()
    print('product likes incremented')


channel.basic_consume(queue= 'admin', on_message_callback = callback, auto_ack=True)

print('started Consuming...')

channel.start_consuming()

channel.close()