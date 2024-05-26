def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
print("Select Operation")
print("1.Add")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
while True:
    choice=input("Enter the choice(1/2/3/4):")
    if choice in('1','2','3','4'):
          try:
                num1=float(input("Enter the First number:"))
                num2=float(input("Enter the Second number:"))
          except ValueError:
                print("Invalid input.Enter a number:")
          continue
    if choice =='1':
        print(num1 ,"+",num2,"=",add(num1,num2))
    elif choice =='2' :
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice =='3':
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif choice =='4':
        print(num1,"/",num2,"=",division(num1,num2))
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
          break
    else:
        print("Invalid Input")



        



