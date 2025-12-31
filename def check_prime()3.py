def check_prime():
    num = int(input("Enter a number: "))

    if num <= 1:
        print(num, "is NOT a Prime number")
        return

    for i in range(2, num):
        if num % i == 0:
            print(num, "is NOT a Prime number")
            break
    else:
        print(num, "is a Prime number")

# Function call
check_prime()
