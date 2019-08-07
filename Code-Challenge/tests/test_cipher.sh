# Test the 'cipher' application by running the test cases in 'cases' to ensure that the program:
#  1. parses keys correctly and handles invalid keys
#  2. properly encrypts and decrypts data
#
# Each test case consists of the following files:
#  1. `test.key` A key for the cipher program to read in
#  2. `invalid-key` (optional) indicating that the key is invalid. Omit this file if the key is valid.
#     If the key is invalid the `invalid-key` file's contents describe the error.
#  3. `message.txt` (if key is valid) to encrypt
#  4. `message.txt.encrypted` (if key is valid) to decrypt
#
# This script takes 3 argument: 
#  1. the path to the program under test
#  2. the argument to pass for encryption
#  3. the argument to pass for decryption
#
# If the tests passed, this script exits with code 0.
# If a test failed, errors will be printed and the script will exit with a non-zero exit code.
#
# Example usage:
#  ./test_cipher.sh ../solns/cpp/bin/cipher encrypt decrypt

if [[ $# -ne 3 ]]; then
	echo Expected exactly 3 arguments, received $#
	exit 1
fi

CIPHER=$1
ENCRYPT=$2
DECRYPT=$3

cleanup() {
	# Clean up an files we created
	rm -f ~decrypted ~encrypted
}


# Get all the test cases
for c in cases/*; do
	echo Running ${c}
	if [[ -e ${c}/invalid-key ]]; then
		# This key is invalid so expect a failure
		${CIPHER} ${ENCRYPT} "${c}/test.key" &>/dev/null
		if [[ $? -eq 0 ]]; then
			# The script did not fail, but it should have
			echo Error ${c}: expected script to fail because of invalid key: $(cat "${c}/invalid-key")
			$(cleanup)
			exit 1
		fi
	elif [[ ! -e "${c}/invalid-key" ]]; then
		# This is a valid substitution key so we should not expect any failures
		${CIPHER} ${ENCRYPT} "${c}/test.key" < "${c}/message.txt" > ~encrypted
		if [[ $? -ne 0 ]]; then
			echo Error ${c}: expected encryption to succeed but it failed
			$(cleanup)
			exit 1
		fi

		if diff ~encrypted "${c}/message.txt.encrypted"; then
			# The encrypted file matches! Try decrypting now.
			${CIPHER} ${DECRYPT} "${c}/test.key" < "${c}/message.txt.encrypted" > ~decrypted
			if [[ $? -ne 0 ]]; then
				echo Error ${c}: expected decryption to succeed but it failed
				$(cleanup)
				exit 1
			fi

			diff ~decrypted "${c}/message.txt"
			if [[ $? -ne 0 ]]; then
				echo Error ${c}: unexpected decrypted message. Expected it to match 'message.txt' 
				$(cleanup)
				exit 1
			fi
		elif [[ $? -ne 0 ]]; then
			# The files are different
			echo Error ${c}: unexpected encrypted message. Expected it to match 'message.txt.encrypted' 
			$(cleanup)
			exit 1
		fi
	fi 
done

$(cleanup)
