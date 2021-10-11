num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
calc = input("Enter operator (+ or - or * or /)): ")

if calc == "+":
    result = float(num1) + float(num2)
elif calc == "-":
    result = float(num1) - float(num2)
elif calc == "*":
    result = float(num1) * float(num2)
elif calc == "/":
    result = float(num1) / float(num2)

print(result)
