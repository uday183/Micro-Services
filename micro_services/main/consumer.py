import pika, json
from main import Product, db
params = pika.URLParameters('amqps://epkkwwwl:4CN0Sg0ztKcS7MWBSK2X-J7LOCAs7hDL@puffin.rmq2.cloudamqp.com/epkkwwwl')


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue= 'main')


def callback(ch, method, properties, body):
    print('received main...')
    data = json.loads(body)
    #print(data)

    if properties.content_type == 'product_created':
        product = Product(product_id=data['id'], title=data['title'],image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('product_created')

    elif properties.content_type == 'product_updated':
        product = Product.query.filter_by(product_id=data['id']).first()
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('product_updated')

    elif properties.content_type == 'product_deleted':
        print(data,'deleted data')
        product = Product.query.filter_by(product_id=data).first()
        db.session.delete(product)
        db.session.commit()
        print('product_deleted')


channel.basic_consume(queue= 'main', on_message_callback = callback, auto_ack=True)

print('started Consuming...')

channel.start_consuming()

channel.close()