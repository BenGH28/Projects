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
#include<fstream>
using namespace std;


int main()
{
  fstream file;
  // ofstream ofile;
  string fname, s;
  char ans;

  cout <<"What file would you like to encrypt?"<<endl;
  cin >> fname;
  file.open(fname);

  if(file.fail())
    cerr << "error opening" << endl;
  else
    {
      while(getline(file, s))
	{
	  for(int i = 0; i < s.size(); i++)
	    {
	      cout<< static_cast<int>(s[i]);
	      file << static_cast<int>(s[i]);
	      file<< "hello"; 
	    }
	}
    }
  /* cout << "would you like to change it back? (Y/N) ";
  cin >> ans;
  if(ans == tolower('Y'))
    {
      for(int i = 0; i < s.length(); i++)
	file<< static_cast<char>(s[i]);
	}*/
  file.close();
  
  return 0;
}

		 

  
  
  
