try:
    number = int(input("Enter a number: "))
    print(number)
    number=number/0
except ZeroDivisionError:
    print("Divided by zero " + err )
except ValueError:
    print("Invalid input " + err)

