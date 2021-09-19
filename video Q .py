# file=open("student txt","r")
# value=file.read()
# print(value)




number=int(input("enter the number"))
modulus=number%10
if modulus%3==0:
    print(modulus,":last digit is divisible by 3")
else:
    print(modulus,":last digit is not divisible by 3")