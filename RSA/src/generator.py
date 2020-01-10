"""A toy RSA module."""
import secrets
from math import gcd
from random import randint
from primeCheck3 import isPrime


def makePrimes(bits):
    """
    Generates the prime numbers p and q.  

    Param bits: int -- the bit length of each prime  

    Returns a tuple of prime numbers.
    """
    p = None
    q = None
    for _ in range(500):
        p = secrets.randbits(bits)
        q = secrets.randbits(bits)
        if p != q and p > 3 and q > 3 and isPrime(p) == True and isPrime(q) == True:
            return (p, q)


def totient(p, q):
    """Computes Eulers totient.

    Params:
        p: int -- a prime number. 
        q: int -- a prime number.

    Returns an int -- the totient value of p * q.
    """
    if p == q:
        raise ValueError("Totient function requires dissimilar inputs")
    return (p-1)*(q-1)


def makeN(p, q):
    """Where we compute the modulus value.

    Params:
        p: int -- a prime number.
        q: int -- a prime number.

    Returns an int-- the modulus value.
    """
    return p * q


def makePubKey(tot, n):
    """Creating the public key based on the totient of the modulus and the modulus itself.

    Params:
        tot: int -- the totient value. 
        n: int -- the modulus value.

    Returns a tuple.
    """
    e = 0
    while(gcd(tot, e) != 1):
        e = randint(2, tot)
    return (e, n)


def extEuclid(e, tot):
    """The extended Euclidian algorithm for determining 'd' the private key.

    Params:
        e: int -- The public key used for encryption.
        tot: int -- The totient value.

    Returns:
        int -- 'd' the private decryption key if inverse exists.
        None -- if there is no inverse.
    """
    n_zero = tot
    b_zero = e
    t_zero = 0
    t = 1
    q = n_zero // b_zero
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
    """Making the private key.

    Params:
        e: int -- The public encryption key.
        tot: int -- The totient value.
        n: int -- The modulus value.

    Returns a tuple.
    """
    while True:
        d = extEuclid(e, tot)
        if d != e:
            break
    return (d, n)


def gen(bits):
    """Generates the public and private keys.

    Param bits: int -- bit length for prime generation.

    Returns a tuple of tuples.
    """
    p, q = makePrimes(bits)
    tot = totient(p, q)
    n = makeN(p, q)
    PU = makePubKey(tot, n)
    print(f"public key is: {PU}")
    e, _ = PU
    PR = makePvtKey(e, tot, n)
    print(f"private key is: {PR}")
    return (PU, PR)


if __name__ == "__main__":
    PU, PR = gen(8)

    # encryption
    e, n = PU
    d, _ = PR
    m = 50
    print(f"original message: {m}")
    cipher = (m ** e) % n
    print(f"cipher {cipher}")

    # decryption
    message = (cipher ** d) % n
    print(f"message: {message}")
