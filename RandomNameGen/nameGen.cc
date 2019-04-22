/* This is a program to generate random names.
1) seperate letters into arrays of vowels and consonants.
2) choose if the name starts with vowel or consonant.
3) to keep things simple: if name starts with vowel next letter will be consonant.
4) if name begins with consonant it is followed by a vowel and alternates afterwards.*/

#include<iostream>
#include<cstdlib>
#include<ctime>
#include<cctype>
using namespace std;

int main()
{
  srand(time(0));
  unsigned int size = rand() % 8 + 3; //random size of name array from 3 to 10
  char vow[6] = {'a','e','i','o','u','y'};
  char con[21] = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'};
  char name[size+1];
  int choice = rand()%2; //choose if the name starts with vowel or consonant
  cout << "Choice: " << choice << endl
       << "Size: " << size << endl;
  if(choice == 0){
    for(unsigned int i = 0; i < size; i++){
      if(i % 2 == 0)
        name[i] = vow[rand() % 6];
      else
        name[i] = con[rand() % 21];
    }
  }
  else{
    for(unsigned int i = 0; i < size; i++){
      if(i % 2 ==0 )
        name[i] = con[rand() % 21];
      else
        name[i] = vow[rand() % 6];
    }
  }
  name[size] = '\0';
  name[0] = toupper(name[0]);
  cout <<"Your name is: " << name << endl;
  return 0;
}
