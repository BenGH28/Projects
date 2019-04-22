//************************************************************************
//My first attempt at encryption.
//Author: Ben Hunt
//this is my thought process:
//
//step 1: convert everything to ascii.  This works when I print to
//terminal, however when I actually try to change the file itself it semi
//works --further research needed
//
//step 2: I need to actuall change the data. Conversion does nothing
//apart from turning to numbers.
//
//step 3: Need to be able to decrypt what I have encrypted.
//another function or another file altogether?
//For to come on that front.
//************************************************************************

#include<iostream>
#include<string>
#include<queue>
using namespace std;

void toAscii(string&, int);
void onQ(string&, queue<int>&, int);
void readQ(queue<int>&);
void encrypt(string&);
void decrypt(string&, queue<int>&);

int main()
{
  queue<int> decr;
  string message, enMess;
  int choice;


  cout << "Press 1 for encryption or 2 for decryption: ";
  cin >> choice;
  do{
    if(choice == 1)
      encrypt(message);
    else
      decrypt(enMess, decr);

    cout<< "Press 1 for encryption or 2 for decryption or 0 to quit: ";
    cin >> choice;

    //reset
    message = "";
    enMess = "";
    cout << endl;
    }
  while (choice == 1 || (choice == 2));
  return 0;
}


void toAscii(string& a, int key){ //converting message to ascii code and multiplying by the key
  for(unsigned int i = 0; i < a.size(); i++)
    cout<< static_cast<int>(a[i]) * key << " ";
  cout << endl;
}
void onQ(string& a, queue<int>& b, int key){//where the parsing of the encrypted message happens
  int j = 0;//the start of he word
  string sub;//the word that is pushed to queue
  int num; //the string of numbers now an integer
  for(unsigned int i = 0; i < a.size(); i++){
    if(a[i] == ' ' && j == 0){ //beginning edge case
      sub = a.substr(j,i);
      num = stoi(sub) / key;
      b.push(num);
      j = i+1;
    }
    else if(i == a.size()-1){ //end edge case
      sub = a.substr(j, ((i-j)+1));
      num = stoi(sub) / key;
      b.push(num);
    }
    else if(a[i] == ' '){//everthing in between
      sub = a.substr(j,i-j );
      num = stoi(sub) / key;
      b.push(num);
      j = i + 1;
    }
  }
}
void readQ(queue<int>& q){
  int asciiInt;
  char asciiChar;
  string dMess = "";
  while(!q.empty()){
    asciiInt = q.front();
    asciiChar = asciiInt;
    dMess += asciiChar;
    q.pop();
  }
  cout << endl << "Your message is: " << dMess << endl;
}
void encrypt(string& a){
  int key = 0;
  cout << "Enter the message you would like to encrypt?" <<endl;
  cin.ignore();
  getline(cin, a);
  cout << "Please enter a key to complete encryption"<<endl;
  cin >> key;
  toAscii(a,key);
}
void decrypt(string& a, queue<int>& q){
 int key = 0;
 cout << "Enter the encrypted message below." << endl;
 cin.ignore();
 getline(cin, a);
 cout << "Please enter the decryption key: ";
 cin >> key;
 onQ(a, q, key);
 readQ(q);
}
