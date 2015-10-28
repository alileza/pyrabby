from pyrabby import Rabby, test

a = Rabby('localhost', 'hello')

z = dict(
        name="Joni"
    )

a.send(z)
