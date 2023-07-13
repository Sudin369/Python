#prime or composite
for i in range(1,10,1):
 def prime(no):
    c=0
    for y in range(1,no+1,1):
        if no%y==0:
            c+=1
    if c<=2:
        return True
    else:
        return False

 no=int(input("enter input: "))
 if prime(no)==True:
    print(f"{no} is prime")
 else:
    print(f"{no} is composite")