#include<NTL/ZZ_p.h>
#include <NTL/ZZ.h>
#include<NTL/ZZ_pXFactoring.h>
#include<NTL/vector.h>
using namespace std;
using namespace NTL;

int main()
{

   ZZ n1,n2,p1,p2,q,f,n_cpy; 

   long L = 512;
	int err = -1;
   GenGermainPrime(p1,L,err);
   GenGermainPrime(p2,L,err);
   GenGermainPrime(q,L,err);
   n1 = p1*q;
   n2 = p2*q;

   cout <<"P1="<< p1 << "\n";
   cout <<"P2="<< p2 << "\n";
   cout <<"Q="<< q << "\n";
   cout <<"N1="<< n1 << "\n";
   cout <<"N2="<< n2 << "\n";
   //~ ZZ d;
   //~ GCD(d, n1,n2);
   //~ cout <<"GCD="<< d << "\n";
   //~ if(d == q){
	   //~ cout <<"GCD is correct"<< "\n";
	   //~ }
   return 0;
}



