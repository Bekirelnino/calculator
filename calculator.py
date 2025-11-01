num1=float(input("Enter first number:"))
operation=input("Enter operation(+,-,*,/):").strip()
num2=float(input("Enter second number:"))
if operation=="+":
    print("result=",num1+num2)
elif operation=="-":
 print("result is:",num1-num2)
elif operation=="*":
   print("result is:",num1*num2)
elif operation=="/":
    if num2 != 0:
        print("result is:",num1/num2)
    else:
        result="Error! Division by zero"
else:
    result="Invalid operation"
    print(f"Result: {result}")
input("Press enter to continue...")