order = '1,2013-07-25 00:00:00.0,11598,CLOSED'
orderStatus = order.split(",")
print(orderStatus)
print(orderStatus[3])
print(orderStatus[0])
print(type(orderStatus[0]))

print(10 > 2)
print('10' > '2')

print(int(orderStatus[0]))

if(orderStatus[0].isdigit()):
    i = orderStatus[0]

print(i)
