def area_rectangle():
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))
    area = length * breadth
    return area

# Function call
result = area_rectangle()
print("Area of Rectangle =", result)
