from pyrabby import Rabby, test

a = Rabby('localhost', 'hello')

def callback(body):
    print body['name']

a.listen(callback)
