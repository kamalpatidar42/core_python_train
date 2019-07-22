topic = """
                Introduction to logical Operators.
                    and, or, not
 """
a = 11
b = 2
c = 20
print(topic)
res = c > a and c > b
print(a, b, c, res)
res = c > a > b
print(a, b, c, res)

# Ternary Operator
topic = """
                Ternary Operator demo
                <True Value> if <condition> else <false value> 
 """
print(topic)
a = 15
b = 2
c = a if a > b else b
print(a, b, c)
print(a, " --> Even " if a % 2 == 0 else " --> odd")
