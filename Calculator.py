print("\033c")

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
op = input("Enter operator (+, -, x, /) : ")

if op == "+":
    res = add(num1, num2)
    print(f"Sum of {num1} + {num2} = {res}")

elif op == "-":
    res = sub(num1, num2)
    print(f"Subtraction of {num1} - {num2} = {res}")

elif op == "x":
    res = mul(num1, num2)
    print(f"Product of {num1} x {num2} = {res}")

elif op == "/":
    res = div(num1, num2)
    print(f"Division of {num1} / {num2} = {res}")