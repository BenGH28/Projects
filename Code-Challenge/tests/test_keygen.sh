#!/usr/bin/env bash

# Test that the 'keygen' program behaves properly.
# Arguments:
#    KEYGEN: The path to the 'keygen' program under test.

KEYGEN=$1

set -e  # make every command call that fails exit the program

if [[ $# -ne 1 ]]; then
	echo "ERROR: expected exactly one argument: the path to the 'keygen' program under test"
	exit 1
fi

# Call the function multiple times as quickly as possible and check that each key is different
keys=()  # Array of keys ot check later
for i in {0..50}; do
	first=$(${KEYGEN})
	second=$(${KEYGEN})
	if [[ $first == $second ]]; then
		echo "ERROR: successive calls to '${KEYGEN}' produced the same output"
		exit 1		
	fi
	# Push the key onto keys for validation later
	keys+=("${first}")
	keys+=("${second}")	
done

# Validate each key
for key in "${keys[@]}"; do
	echo "${key}" | ./check_key
done

