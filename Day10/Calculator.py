import art
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    if n2==0:
        return "Division by zero is not possible!"
    return n1 / n2
operations={"+": add, "-": sub, "*": mul, "/": div}
loop_over=False
result=0
while not loop_over:
    print("Welcome to the Calculator!")
    print(art.logo)
    n1=float(input("Enter the first number: "))
    operator=input("Enter a mathematical operator( + for addition, - for subtraction, * for multiplication, / for division): ")
    n2=float(input("Enter the second number: "))
    result=operations[operator](n1,n2)
    print(f"The result is: {result}")
    loop_over1 = False
    while not loop_over1:
        continue_or_not=input("Would you like to continue? (Yes/No): ").lower()
        if continue_or_not=="yes":
            operator1=input("Enter the operator: ")
            n3=float(input("Enter the number: "))
            result=operations[operator1](result,n3)
            print(f"The result is: {result}")
        if continue_or_not=="no":
            loop_over1=True
            print("\n"*100)





