def even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function call
result = even_odd()
print("Number is", result)
