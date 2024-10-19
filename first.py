## this is how we do it

'''
this is how we do it
'''

## declaring variables 
name = 'Charles'
number_one = 12 
number_two = 3.12
status = False 

print(type(name))
print(type(number_one))
print(type(number_two))
print(type(status))
print(number_one+number_two)

## a returning function
def Subtraction():
    diffrence = number_one + number_two
    return diffrence
print(Subtraction())

## a void function
def Addition():
    sum = number_one + number_two
    print(sum)

Addition()
