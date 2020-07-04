i = 0
print(type(i))
order = '1,2013-07-25 00:00:00.0,11598,CLOSED'

s = '1'
print(type(s))
i = int(s)
print(type(i))

s = 'a'
print(type(s))
#i = int(s) # should get a value error

s = '1.5'
f = float(s)
print(f)
type(f)
print(type(f))

i = 20130725
s = str(i)

d = 20200704
#print("Today's date is " + d) # will give a type error
print("Today's date is " + str(d))
