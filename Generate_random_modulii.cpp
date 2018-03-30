#include<NTL/ZZ_p.h>
#include <NTL/ZZ.h>
#include<NTL/ZZ_pXFactoring.h>
#include<NTL/vector.h>
using namespace std;
using namespace NTL;

int main()
{

   ZZ n1,n2,p1,p2,q,f,n_cpy; 

   long L = 512*4;

   GenGermainPrime(p1,L,800);
   GenGermainPrime(p2,L,800);
   GenGermainPrime(q1,L,800);
   GenGermainPrime(q2,L,800);
   n1 = p1*q1;
   n2 = p2*q2;

   cout <<"P1="<< p1 << "\n";
   cout <<"P2="<< p2 << "\n";
   cout <<"Q1="<< q1 << "\n";
   cout <<"Q2="<< q2 << "\n";
   cout <<"N1="<< n1 << "\n";
   cout <<"N2="<< n2 << "\n";
   //~ ZZ d;
   //~ GCD(d, n1,n2);
   //~ cout <<"\n\nGCD="<< d << "\n";
   //~ if(d == 1){
	   //~ cout <<"GCD is correct"<< "\n";
	   //~ }
   return 0;
}



