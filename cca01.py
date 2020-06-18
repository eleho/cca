i = 0
i = "Hello"
i = 10.5
print(type(i))

#val i = 100
i = 100
print(type(i))

if(i % 2 == 0):
    print(str(i) + " is an integer number")
else:
    print(str(i) + " is not an integer number")

def CheckEven(j):
    if(j % 2 == 0):
        print(str(j) + " is an even number")
    else:
        print(str(j) + "is an odd number")

print(CheckEven(2))

# first comment
print("Hello World!") #comment no-2

word = 'word'
sentence = "This is a sentence"
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

print(word)
print(sentence)
print(paragraph)

counter = 100
name = "Alex"
seconds = 10.5

a = b = c = 10

print(a)
print(b)
print(c)

a = a + 1

print(a)
print(b)
print(c)

p, q, r = 1, 2.5, "john"

print(p)
print(q)
print(r)

i = 0
l = [1, 2, 3, 4]
s = {1, 2, 3, 4}
d = {"key1" : "value1", "key2" : "value2"}
t = (1, 2)

print(type(i))
print(type(l))
print(type(s))
print(type(d))
print(type(t))
