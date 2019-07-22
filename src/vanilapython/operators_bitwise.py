topic = """
                Introduction to Bitwise Operators.
                    <<, >>, ~, ^, &, |
 """
a = 0xff  # 0000 0000 1111 1111
b = 2
print(topic)
# Printing binary, hexadecimal, octa binary format of a number.
print(a, bin(a), hex(a), oct(a))
# If you notice here python only saves required bits
print(b, bin(b), hex(b), oct(b))
print('and operator', a & b)
print('or operator', a | b)
print('Left shift', a << b)
print('Right shift', a >> b)
print('XOR', a ^ b)
print('Not', ~a)
