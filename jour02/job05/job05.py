def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2


print(calcule(4, "+", 2))
print(calcule(4, "*", 4))
print(calcule(4, "-", 2))
print(calcule(5, "/", 1))
print(calcule(2, "%", 10))
