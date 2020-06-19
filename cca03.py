var = 10
var1 = 0
if var:
    print("Value of var is " + str(var))

if var1:
    print("Value of var1 is " + str(var1))
print("Note condition was not met so nothing printed")

if not var1:
    print("Value of var1 is " + str(var1))

# what you want is
if var1:
    print("Value of var1 is " + str(var1))
else:
    print("Value of var1 is equal to zero")

if var <= 50:
    print("Value of var is less than 50")
    if var > 30 and var <= 50:
        print("Value of var is between 31 and 50")
    elif var > 10 and var <= 30:
        print("Value of var is between 11 and 30")
    else:
        print("Value of var is less than or equal to 10")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(5):
    print(x)

for x in range(1, 10):
    if x % 2 == 0:
        print(x)

for x in range(1, 10):
    if x % 2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

#for x in range(1, 10):
#    print(str(x) + " is even") if(x % 2 == 0) else print(str(x) + " is odd")
#Above only seems to work when run directly in the terminal
