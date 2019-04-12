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
#include<fstream>
using namespace std;

void toAscii(string&);
void onQ(string&, queue<int>&);
void readQ(queue<int>);
void encrypt(string&);
void decrypt(string&, queue<int>&);

int main()
{
  queue<int> decr;
  string message, enMess;
  char ans;
  int choice;
  cout << "Press 1 for encryption or 2 for decryption: ";
  cin >> choice;
  
  if(choice == 1){
    encrypt(message);
  }
  else{
    decrypt(enMess, decr);
  }
  return 0;
    
}

		 
void toAscii(string& a)
{
  for(int i = 0; i < a.size(); i++){
    cout<< static_cast<int>(a[i]) << " ";
  }
      cout << endl;
}
  
void onQ(string& a, queue<int>& b){
  int j = 0;
  string sub;
  int num;
  for(int i = 0; i < a.size(); i++){
    if(a[i] == ' ' && j == 0){ //beginning edge case	
      sub = a.substr(j,i);
      num = stoi(sub);
      b.push(num);
      j = i+1;
    }
    else if(i == a.size()-1){ //end edge case
      sub = a.substr(j, ((i-j)+1));
      num = stoi(sub);
      b.push(num);
    }
    else if(a[i] == ' '){
      sub = a.substr(j,i-j );
      num = stoi(sub);
      b.push(num);
      j = i + 1;
    }
  }
}
void readQ(queue<int> q){
  int asciiInt;
  char asciiChar;
  string dMess = "";
  while(!q.empty()){
    asciiInt = q.front();
    asciiChar = asciiInt;
    dMess += asciiChar;
    q.pop();
  }
  cout << "Your message is: " << dMess << endl;
}
void encrypt(string& a){
  cout <<"Enter the message you would like to encrypt?"<<endl;
  cin.ignore();
  getline(cin, a);
  toAscii(a);
}
void decrypt(string& a, queue<int>& q){
 cout <<"Enter the encrypted message below." << endl;
 cin.ignore();
 getline(cin, a);
 onQ(a, q);
 readQ(q);
}


    
  
  
  
  
  
