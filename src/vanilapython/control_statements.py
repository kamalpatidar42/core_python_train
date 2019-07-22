topic = '''
            Introduction to Control Statements
Description of if -
    if <condition>:
        statement 1 --> statements under if
        statement 2 --> statement under if
    statement3 --> Out of if statement
    
Description of else - 
    if <condition>:
        statement 1 --> statements under if
        statement 2 --> statement under if
    else:
        statement3 --> under else statement
    statement4 --> out of if else
    
Description of else if - 
    if <condition>:
        statement 1 --> statements under if
        statement 2 --> statement under if
    elif:
        statement3 --> under else if
    else:
        statement4 --> under else
    statement 5 -> out of if else
    
@Note : Python is indentation sensitive.
'''
print(topic)
condition = True

if condition:
    print("statement1")
print("+"*50)

condition = False
if condition:
    print("statement1")
    print("statement2")
else:
    print("statement4")
print("+"*50)

elseif_condition = True

condition = False
if condition:
    print("statement1")
    print("statement2")
elif elseif_condition:
    print("statement3")
else:
    print("statement4")
print("+"*50)
