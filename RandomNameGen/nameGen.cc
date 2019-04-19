/* This is a program to generate random names.
1) seperate letters into arrays of vowels and consonants.
2) choose if the name starts with vowel or consonant.
3) to keep things simple: if name starts with vowel next letter will be consonant.
4) if name begins with consonant it is followed by a vowel and alternates afterwards.*/

#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

void print(char ch[], int a){
  for(int i = 0; i < a; i++)
    cout << ch[i];
  cout << endl;
}

int main()
{
  srand(time(0));
  int size = rand()%8 + 3; //random size of name array from 3 to 10
  int first = 0, next = 1;
  char vow[5] = {'a','e','i','o','u'};
  char con[21] = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'};
  char name[size];
  int choice = rand()%100;//random number between 0 and 100 to choose
                          //what letter the name begins with
  cout << "Choice: " << choice << endl
       << "Size: " << size << endl;
/*  while (first < size) {
    if(choice % 2 == 0){
      name[first] = vow[rand()%6];
      name[next] = con[rand()%22];
      first += 2;
      next += 2;
      if (next == size)
        name[first] = vow[rand()%6];
    }
    else{
      name[first] = con[rand()%22];
      name[next] = vow[rand()%6];
      first += 2;
      next += 2;
      if (next == size)
        name[first] = vow[rand()%6];
    }
  }*/
  if(choice % 2 == 0){
    for(int i = 0; i < size; i++){
      name[first] = vow[rand()%6];
      name[next] = con[rand()%22];
      if (next < size){
        first += 2;
        next += 2;
      }
      cout << "First: " << first << " Next: " << next << endl;
    }
  }
  else{
    for(int i = 0; i < size; i++){
      name[first] = con[rand()%22];
      name[next] = vow[rand()%6];
      if (next < size){
        first += 2;
        next += 2;
      }
      cout << "First: " << first << " Next: " << next << endl;
    }
  }
  print(name,size);
  return 0;
}
