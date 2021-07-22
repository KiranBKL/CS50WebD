import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
# THis Causes Syntax error except ZeroDivisionError,ValueError:
except(ZeroDivisionError,ValueError):
    print("Error: Cannot divide by 0")
    sys.exit(1)
finally:
    print("This is always excuted")

print(f"x / y = {result}")
