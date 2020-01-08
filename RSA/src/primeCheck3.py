from math import sqrt, ceil


def isPrime(x):
    prime = True
    if x <= 0:
        return "number must be greater than zero"
    elif x == 2 or x == 3:
        return prime
    else:
        for i in range(2, ceil(sqrt(x)) + 1):
            if x % i == 0:
                prime = False
                return f"{prime}, divisible by, {i}"
        return prime


if __name__ == "__main__":
    strNum = input("Enter number to check if prime (-1 to quit): ")
    while strNum != '-1':
        num = int(strNum)
        print(isPrime(num))
        strNum = input("Enter number to check if prime (-1 to quit): ")
