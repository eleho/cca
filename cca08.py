s = "Hello"
print(s*4)

def say(s, times=1):
    print(s * times)

say("Hello ")

say("Hello ", 4)

def func(a, b=5, c=10):
    print('a is ' + str(a) + "; b is " + str(b) + "; c is " + str(c))

func(3, 7)
func(25, c=24)
func(c=50, a=100)

def total(initial=5, *numbers):
    count=initial
    for num in numbers:
        count += num
    return count

print(total(10, 1, 2, 3, 4))

def total(initial=5, *numbers, **keywords):
    count=initial
    for num in numbers:
        count += num
    for key in keywords:
        count += keywords[key]
    return count
    
print(total(10, 1, 2, 3, vegetables=50, fruits=100))
