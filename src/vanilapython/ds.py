topic = """
        Basic Data Structures
"""
print(topic)

a = []
b = ()
c = {}
print('type(a)', type(a))
print('type(b)', type(b))
print('type(c)', type(c))

a = list()
b = tuple()
c = dict()
print("line".center(40))
print('type(a)', type(a))
print('type(b)', type(b))
print('type(c)', type(c))
print("\n" * 5)
# Lists
list0 = [1, 2, 3, 5, 6, 7, 8, 9]
list1 = [10, 20, 30, 50, 60, 70, 80, 90]
list2 = [10, 20, 30, 50, 60, 70, 80, 90]
list3 = list([1, 2, 4, 5, 6])
list4 = list([1, 2, 4, 5, 6])

# Joining two lists union.
list_res = list0 + list1
print(list0)
print(list1)
print(list_res)
print(id(list1))
print(id(list2))
# Applying traversal techniques used in collection_traversal.py.
print(list_res[0:4])
print(list_res[0::2])
print(id(list3))
print(id(list4))
print("""
@Note: Python preserves immutable values and allocates reference to variables. Whereas, list are mutable object.
 So, despite having same value new memory is allocated. Which was not the case for string.  
""")
for val in list_res:
    print(val, end=" ")
# Proof of mutability.
list0[1] = 100


# Tuple
tuple_1 = (1, 123.2, 'hello', 'are', 5, 6, 7)
tuple_2 = (1, 123.2, 'hello', 'are', 5, 6, 7)
print("""trying mutability for tuple:
tuple_1[1] = 100
error: 
  tuple_1[1] = 100

TypeError: 'tuple' object does not support item assignment
if you see Id of below print statements it shows that python preserves the branch.
print(id(tuple_1))
print(id(tuple_2))
Output:
""")
print(id(tuple_1))
print(id(tuple_2))
