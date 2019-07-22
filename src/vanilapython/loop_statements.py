topic = '''
            Introduction to Control Statements (Loops)
Description of while -
    while <condition>:
        statement 1 --> looping statement
        statement 1 --> looping statement
    statement3 --> Out of while statement
Sample code:
    cnt = 1
    while cnt <= 10:
        print(cnt, end = " ")
        cnt = cnt + 1
Output: 
1 2 3 4 5 6 7 8 9 10 
    
Description of for - 
    for <count_variable> in <collection>:
        statement 1 --> statements under if
Sample code:
    for cnt in range(1,11):
        print(cnt, end = " ")
Output: 
1 2 3 4 5 6 7 8 9 10 
     
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
cnt = 5
while cnt <= 10:
    print(cnt, end=" ")
    cnt = cnt + 1
print("\n")

# Range returns range type of object.
for cnt in range(1, 11):
    print(cnt, end=" ")
print(range(1,10))