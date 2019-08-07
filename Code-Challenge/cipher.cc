#include <algorithm>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
using namespace std;

typedef map<int, int> enMap;
void keyCheck(ifstream &);
void readIn(ifstream &, enMap &);
void reverse(enMap &, enMap &);

int main(int argc, char *argv[]) {
	enMap keyCode;
	enMap rKeyCode; // the reversed encryption key for decryption
	string enMess = "", message = "";
	uint8_t ch;
	ifstream kFile;

	kFile.open(argv[2]);

	if(argc == 1) {
		cout << "Usage: ./cipher [command] [key] <file name here> [output file]\n";
		cout << "Commands: \nencrypt \ndecrypt\n";
	} else if(strcmp(argv[1], "encrypt") == 0) {
		readIn(kFile, keyCode);
		while(getline(cin, message)) {
			for(int i = 0; i < message.size(); i++) {
				ch = message[i];
				ch = keyCode[ch];
				enMess += ch;
			}
			message = "";
		}
		cout << enMess;
	} else if(strcmp(argv[1], "decrypt") == 0) {
		readIn(kFile, keyCode);
		reverse(keyCode, rKeyCode);
		getline(cin, enMess);
		for(int i = 0; i < enMess.size(); i++) {
			ch = enMess[i];
			ch = rKeyCode[ch];
			message += ch;
		}
		cout << message;
	}
	return 0;
}

/*void keyCheck(ifstream &keycode) {
  if(keycode.fail()) {
    cout << "ERROR: keycode does not exist.\n";
  }
  for(keycode >> real >> change; !keycode.eof(); keycode >> real >> change) {
    if(keycode[] > 255 && keycode[i] < 0) {
      cout << "ERROR: keycode out of bounds\n";
    }
  }
}*/
void readIn(ifstream &file, enMap &myKey) {
	int real, alt;
	while(file >> real >> alt) {
		myKey[real] = alt;
	}
}

void reverse(enMap &en, enMap &de) {
	for(auto i = begin(en); i != end(en); ++i) {
		de[i->second] = i->first;
	}
}