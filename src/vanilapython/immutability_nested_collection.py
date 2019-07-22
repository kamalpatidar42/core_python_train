list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
list3 = [100, 200, 300, 400]
tuple1 = (1, 2, 3, 4)
tuple2 = (10, 20, 30, 40)
tuple3 = (100, 200, 300, 400)

list_of_lists = [list1, list2, list3]
tuple_of_lists = (list1, list2, list3)
list_of_tuples = [tuple1, tuple2, tuple3]
tuple_of_tuples = (tuple1, tuple2, tuple3)

# Trying to change the nested element.
list_of_lists[0][1] = 123
print(list_of_lists)
# Will it work?
tuple_of_lists[0][1] = 123
print(tuple_of_lists)

# Will it work?
# Compilation error:  Tuple does not support assignment.
# tuple_of_lists[0] = [1,2,3,4]
#    list_of_tuples[0][1] = 10000
# TypeError: 'tuple' object does not support item assignment
# list_of_tuples[0][1] = 10000
