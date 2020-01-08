import math
from math import gcd, floor, fabs
from random import randint
from primeCheck3 import isPrime

# a little module created to generate and calculate the various
# functions required for RSA


def makePrimes(a, b, c, d):
    try:
        p = randint(a, b)
        q = randint(c, d)
    except ValueError:
        print(f"ensure {a} < {b} and {c} < {d}")
        return -1

    for _ in range(100):
        if isPrime(p) == True and isPrime(q) == True:
            return (p, q)
        p = randint(a, b)
        q = randint(c, d)
    return (-1, -1)


def totient(p, q):
    return (p-1)*(q-1)


def makeN(p, q):
    return p*q


def makePubKey(tot, n):
    e = 0
    while(gcd(tot, e) != 1):
        e = randint(2, tot)
    return (e, n)


def extEuclid(e, tot):
    n_zero = tot
    b_zero = e
    t_zero = 0
    t = 1
    q = n_zero//b_zero
    r = n_zero - q * b_zero
    while r > 0:
        temp = t_zero - q * t
        if temp >= 0:
            temp = temp % tot
        if temp < 0:
            temp = tot - ((-temp) % tot)
        t_zero = t
        t = temp
        n_zero = b_zero
        b_zero = r
        q = n_zero//b_zero
        r = n_zero - q * b_zero
    if b_zero != 1:
        print("no inverse")
        return None
    else:
        return t % tot


def makePvtKey(e, tot, n):
    while True:
        d = extEuclid(e, tot)
        if d != e:
            break
    return (d, n)


if __name__ == "__main__":
    p, q = makePrimes(1000, 2000, 3000, 4000)
    tot = totient(p, q)
    n = makeN(p, q)
    PU = makePubKey(tot, n)
    PR = makePvtKey(PU[0], tot, n)

    print(f"public key is: {PU}")
    print(f"private key is: {PR}")

    # encryption
    m = 19
    print(f"encrypting {m}")
    power = m ** PU[0]
    cipher = int(power % PU[1])
    print(f"Cipher: {cipher}")

    # decryption
    print(f"decrypting {cipher}")
    power1 = cipher ** PR[0]
    decipher = int(power1 % PR[1])
    print(f"original message: {decipher}")
