def calculate():
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    print("Addition: +/nSubtraction: -/nMultiplication: */nDivision: //nModulus: %/nFloor Division: ///nExponent: **")
    op = input("Enter the operation: ")
    if op =='+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op =='/':
        return a/b
    elif op == "//":
        return a//b
    elif op == "%":
        return a%b
    elif op == "**":
        return a**b
    else:
        print("Invalid Operator")

if __name__ == '__main__':
    print(calculate())

