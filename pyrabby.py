import pika, json

def test():
    print 'hello'

class Rabby:

    def __init__(self, host, q):
        self.q = q
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=host))

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=q)


    def send(self, data):
        data = json.dumps(data)
        self.channel.basic_publish(exchange='',
                              routing_key=self.q,
                              body=data)
        print " [x] Sent %r" % (data,) 

    def listen(self, callback):

        print ' [*] Waiting for messages. To exit press CTRL+C'

        def cb(ch, method, properties, body):
            print " [x] Received %r" % (body,)
            body = json.loads(body)
            return callback(body)

        self.channel.basic_consume(cb,
                              queue=self.q,
                              no_ack=True)

        self.channel.start_consuming()
#
# rabby = Rabby('localhost', 'hello')
