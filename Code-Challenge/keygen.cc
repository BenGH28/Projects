#include <algorithm>
#include <ctime>
#include <iostream>
#include <random>
#include <vector>
using namespace std;

int main() {
	vector<int> code = {};
	vector<int> key  = {};
	// pushing data onto the vectors
	for(int i = 0; i < 256; i++) {
		code.push_back(i);
		key.push_back(i);
	}
	// shuffling the data for key
	for(auto i : key) {
		shuffle(begin(key), end(key), default_random_engine(time(0)));
	}
	// output the entire key to be used
	for(int i = 0; i < 256; i++) {
		cout << code[i] << " " << key[i] << endl;
	}

	return 0;
}
