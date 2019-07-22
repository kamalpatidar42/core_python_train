a = "New string here"

# Another flavor of string

b = ''' Some more string
 added here '''

# Another flavor of string

c = """ Three time variable single 
        Quote.
"""

print(a, b, c)
print('Type of variable a', type(a))
print('Type of variable b', type(b))
print('Type of variable c', type(c))

# Python stores everything on ram and everything is object. Even the primitive type
# in another language are object in python.
# Python generates byte code.
# Since
x = 1000 ** 200
y = 2000 ** 2000
print(x)
print('Type of big integer variable x', type(x))
print('Type of big integer variable y', type(y))
print('location of variable x', id(x))
print('location of variable y', id(y))

# Python assigns new memory only if new value is assigned otherwise it assigns same memory
# Below code, z is assigned value 10 and zzz is again assigned with value 10. This allots same address.
# Even for calculated values if value is same as early it won't assign a new memory.
z = 10
zz = z
zzz = 10
yy = 2 * 5
print('location of variable z', id(z))
print('location of variable zz', id(zz))
print('location of variable zzz', id(zzz))
print('location of variable yy', id(yy))
