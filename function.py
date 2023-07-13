operation = input("Enter operation...!")
first_number = int(input("Enter first number...!"))
second_number = int(input("Enter second number...!"))

def add(num_one,num_two):
    sum = num_one+num_two
    return sum

def sub(num_one,num_two):
    subtract = num_one-num_two
    return subtract

if operation=='+':
    print(add(first_number,second_number))
    
elif operation=='-':
    print(sub(first_number,second_number))