a = '''Introduction to collection traversal'''
print(a)
# Character at index. Output:
print(a[1])
# Starting point to end point (exclusive) Syntax: a[start_index:end_index]. Output:
print(a[1:5])
# Starting point to end point (exclusive) Syntax: a[start_index:end_index], when nothing specified. it takes minimum to
# maximum. Output:
print(a[:])
# Starting point to end point (exclusive) Syntax: a[start_index:end_index], when nothing specified. it takes minimum to
# maximum. Output:
print(a[1:])
# You can provide step also. Syntax is a[start_index:end_index:step]. If you don't provide it takes default.
print(a[1::2])
# Selection of last character.
print(a[-1])
# Reverse selection.
print(a[-1:5])
# Reverse selection with step.
print(a[-1::5])
# Reverse selection with step with end point
print(a[::-5])
