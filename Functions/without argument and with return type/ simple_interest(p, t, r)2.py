def simple_interest(p, t, r):
    si = (p * t * r) / 100
    print("Simple Interest =", si)

p = int(input("Enter Principal: "))
t = int(input("Enter Time: "))
r = int(input("Enter Rate: "))

simple_interest(p, t, r)
