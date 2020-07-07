l = []
print(type(l))
l = [1, 2, 3, 5, 4, 4, 1, 2, 6]
print(type(l))
print(l[0])
print(l[1])
print(l[:3])
print(l[1:5])
print(len(l))
print(l)

s = {}
print(type(s))
s = set({})
print(type(s))
s = {1, 2, 3, 5, 4, 4, 1, 2, 6}
print(type(s))
# print(s[0]) # TypeError
print(s)
print(len(s))

d = {}
print(type(d))
d = {1: 'Hello', 2 : 'World', 1 : 'How are you'}
print(d)
