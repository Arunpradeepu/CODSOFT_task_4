op=["+","-","*","/","%"]
print("The operators are:",op)
n=int(input("Enter the first number:"))
op=input("Enter the operator:")
m=int(input("Enter the second number:"))


if op=="+":
    print("The sum is: ",n+m)
elif op=="-":
    print("The substration is: ",n-m)
elif op=="*":
    print("The multiplication is: ",n*m)
elif op=="/":
    print("The division is: ",n/m)
elif op=="%":
    print("The mod is: ",n%m)

else:
    print("Invalid operator")    