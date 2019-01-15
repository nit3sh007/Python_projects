def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select operation")
print("1.Sum")
print("2,sub")
print("3.multi")
print("4.Divide")

choice=input("enter your choice")
x = int(input("1st number"))
y = int(input("2nd number"))
if choice =='1':
    print(x,"+", y,"=", add(x,y))
elif choice =='2':
    print(x,"-",y,"=", sub(x,y))
elif choice == '3':
    print(x,"*",y,"=", mul(x,y))
elif choice =='4':
    print(x,"/",y,"=",div(x,y))
else:
    print("invalid option")