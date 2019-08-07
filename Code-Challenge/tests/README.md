# Running the tests

## Keygen

To test the 'keygen' program (assuming your implementation is `../solns/cpp/bin/keygen`) call

```sh
./test_keygen.sh ../solns/cpp/bin/keygen
```

If the implementation passes, the script exits with status 0. If it fails, errors will be printed and the script will exit with a non-zero status.

# Cipher

To test the 'cipher' program call

```sh
./test_cipher.sh ../solns/cpp/bin/cipher encrypt decrypt
```

(assuming your program is `../solns/cpp/bin/cipher` and the encrypt/decrypt command line arguments are `encrypt` and `decrypt` respectively.

If the implementation passes, the script exits with status 0. If it fails, errors will be printed and the script will exit with a non-zero status.
