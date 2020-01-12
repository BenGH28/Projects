"""Where RSA cryptography takes place.
This program was created to encrypt the keys required for the Code-Challenge and will only work
with files formatted in like them.

"""

import generator as g
import sys


def intKey(key):
    """Converts a string to tuple of ints

    param key: string -- the key from standard input

    Returns a tuple of ints if correct format or -1 otherwise
    """
    try:
        if key.find(',') != -1:
            newK = key.split(',')
            e = int(newK[0])
            n = int(newK[1])
            k = (e, n)
            return k
        return -1
    except:
        print(
            f"ERROR: invalid key -- '{sys.argv[2]}' is not valid numeric format.\nProper format: 11,17")
        sys.exit()


def crypto(file, key):
    """Cryptographic reading and writing of files.

    Params:
        file: string -- name of file.
        key: tuple of ints
    Returns nothing.
    """
    toWrite = ""
    with open(sys.argv[3], 'r') as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    for line in data:
        member = line.split(' ')
        for value in member:
            if int(value) == 0:
                pass
            if sys.argv[1] == '-e':
                cipher = encrypt(int(value), key)
                toWrite += str(cipher) + " "
            elif sys.argv[1] == '-d':
                decipher = decrypt(int(value), key)
                toWrite += str(decipher) + " "
        file.write(toWrite.strip())
        file.write('\n')
        toWrite = ""


def workOnFile(fileName, key):
    """
    Params:
        fileName: string
        key: tuple of ints
    """
    try:
        with open(fileName, 'w') as c:
            crypto(c, key)
    except FileNotFoundError:
        print(f"ERROR: '{sys.argv[3]}' does not exist.")


def encrypt(m, PU):
    """Encryption

    Param:
        m: int -- value to encrypt
        PU: tuple of ints -- key

    Returns ciphertext
    """
    e, n = PU
    cipher = (m ** e) % n
    return cipher


def decrypt(cipher, PR):
    """Decryption

    Param:
        cipher: int -- value to decrypt
        PR: tuple of ints -- key

    Returns message
    """
    d, n = PR
    decipher = (cipher ** d) % n
    return decipher


if __name__ == "__main__":
    words = ("Commands:\n"
             "   -g     Generate encryption keys and write\n"
             "          them to a document of your choosing.\n"
             "               e.g. RSA.py -g [file_To_Write_To]\n\n"

             "   -e     Encrypt using [key] on [file].\n"
             "               e.g. RSA.py -e <Public,key> [file_To_Encrypt]\n\n"

             "   -d     decrypt a file with a specified key.\n"
             "               e.g. RSA.py -d <Private,key> [file_To_Decrypt]")
    if len(sys.argv) < 2:
        print(
            "General Usage:\n    RSA.py <command> [key] [file]\n"
        )
        print(words)
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-g':
            PU, PR = g.gen(8)
            with open(sys.argv[2], 'w+') as f:
                f.write(f"Public key: {PU}\nPrivate key: {PR}")
        else:
            print(f"ERROR: Invalid Command -- {sys.argv[1]}\n{words}")

    elif len(sys.argv) == 4:
        key = intKey(sys.argv[2])
        if sys.argv[1] == '-e':
            if key != -1:
                workOnFile('output.txt', key)
        elif sys.argv[1] == '-d':
            if key != -1:
                workOnFile('message.txt', key)
        else:
            print(f"ERROR: Invalid Command -- {sys.argv[1]}\n{words}")
    else:
        print(
            f"ERROR: expected 2 or 3 arguments received {len(sys.argv) - 1}\n{words}")
