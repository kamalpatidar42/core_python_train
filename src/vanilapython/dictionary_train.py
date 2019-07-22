dict1 = {'one': 1, 'two': 2, 'three': 3}
print(dict1["one"])
print(dict1.values())
print(type(dict1.values()))
print(dict1.keys())
print(type(dict1.keys()))
for key in dict1.keys():
    print(key, dict1[key])
# TypeError: 'dict_keys' object does not support item assignment
# dict1.keys()[1] = 100
print(dict1.keys())

# List Comprehension
res = [x for x in range(1, 11)]
print(res)

res_1 = [x * x for x in res]
print(res)

res = [x for x in range(1, 11) if x % 2 == 0]
print(res)

res = [x % 2 == 0 for x in range(1, 11)]
print(res)


