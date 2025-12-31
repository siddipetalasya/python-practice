def simple_interest():
    p = int(input("Enter Principal: "))
    t = int(input("Enter Time: "))
    r = int(input("Enter Rate of Interest: "))

    si = (p * t * r) / 100
    print("Simple Interest =", si)

# Function call
simple_interest()
