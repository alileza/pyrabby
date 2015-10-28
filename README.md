# pyrabby

## Client Usage
```python

a = Rabby('localhost', 'communication_key')

data = dict(
        name="Joni"
    )

a.send( data )
```

## Server Usage
```python
a = Rabby('localhost', 'hello')

def callback(body):
    print "Hello %r" % body['name']

a.listen(callback)
```
