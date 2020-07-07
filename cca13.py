t = (1, '2013-07-25 00:00:00.0', 11599, 'CLOSED')
print(t[0])
print(t[3])
print(type(t))

d1 = {1 : 'Hello', 2 : 'World'}
print(d1)
d2 = {1 : 'How are you', 3: 'world'}

d1.update(d2)
print(d1)
print(d1.items())
print(type(list(d1.items())[0]))
