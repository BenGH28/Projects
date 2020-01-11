"""Where RSA cryptography takes place"""

#!/usr/bin/env python3
import generator as g
import os
import sys


def intKey(key):
    if key.find(',') != -1:
        newK = key.split(',')
        e = int(newK[0])
        n = int(newK[1])
        k = (e, n)
        return k
    return -1


def checkKey(key):
    if len(key) == 2:
        if key[0] is int and key[1] is int:
            return True
    return False


def handle(argv, file):
    key = intKey(argv[2])
    if key != -1 and checkKey(key):
        toWrite = ""
        with open(argv[3], 'r') as f:
            data = f.readlines()
        data = [x.strip() for x in data]
        for line in data:
            member = line.split(' ')
            for value in member:
                if int(value) == 0:
                    pass
                if argv[1] == '--e':
                    cipher = encrypt(int(value), key)
                    toWrite += str(cipher) + " "
                elif argv[1] == '--d':
                    decipher = decrypt(int(value), key)
                    toWrite += str(decipher) + " "
            file.write(toWrite.strip())
            file.write('\n')
            toWrite = ""
        file.close()
    else:
        print("Error: invalid key. Valid format is numeric (base 10) CSV notation.\n"
              "     e.g. 19,45")


def encrypt(m, PU):
    e, n = PU
    cipher = (m ** e) % n
    return cipher


def decrypt(cipher, PR):
    d, n = PR
    decipher = (cipher ** d) % n
    return decipher


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print(
            "General Usage:\n    RSA.py <command> [key] [file]\n"
        )
        print(
            "Commands:\n"
            "   -g     Generate encryption keys and write\n"
            "          them to a document of your choosing.\n"
            "               e.g. RSA.py -g file_To_write_to.txt\n\n"

            "   -e     Encrypt using [key] on [file].\n"
            "               e.g. RSA.py -e Public,key file_To_Encrypt.txt\n\n"

            "   -d     decrypt a file with a specified key.\n"
            "               e.g. RSA.py -d Private,key file_To_Decrypt.txt"
        )
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-g':
            PU, PR = g.gen(8)
            with open(sys.argv[2], 'w+') as f:
                f.write(f"Public key: {PU}\nPrivate key: {PR}")

    elif len(sys.argv) == 4:
        if sys.argv[1] == '-e':
            ciphertext = open("output.txt", 'w')
            handle(sys.argv, ciphertext)
        if sys.argv[1] == '-d':
            message = open("message.txt", "w")
            handle(sys.argv, message)
