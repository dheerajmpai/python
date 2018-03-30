#include<NTL/ZZ_p.h>
#include<NTL/ZZ_pXFactoring.h>
#include <NTL/vector.h>
using namespace std;
using namespace NTL;
ZZ encr(ZZ m,ZZ e,ZZ n){
	return PowerMod(m,e,n);
	}
int main()

{
	Vec<ZZ> v;
   ZZ n,p,q,f; 
   long L = 204;
   GenGermainPrime(p,L,800);
   GenGermainPrime(q,L,800);
   n = p*q;
   f=(p-1)*(q-1);
   //~ cout <<"P="<< p << "\n";   cout <<"Q="<< q << "\n";
   //~ cout <<"N="<< n << "\n";
   //~ cout <<"F="<< f << "\n";
   cout <<"Modulo Gen Done" << "\n";
   
   ZZ e=RandomBnd(f),test,d;
   ZZ gcd_ef=ZZ(20);
   while(gcd_ef!=0){
	   e=RandomBnd(f);
	   gcd_ef=InvModStatus(d,e,f);
	   }
	//~ d=InvMod(e,f);
	test=MulMod(e,d,f);
   //~ cout <<"e="<< e << "\n";
   //~ cout <<"d="<< d << "\n";
   //~ cout <<"test="<< test << "\n";
   cout <<"Key Generation Done" << "\n";
   ZZ m = RandomBnd(n);
   ZZ Enc,Dec;
   Enc = encr(m,e,n);
   Dec = encr(Enc,d,n);
   if(m==Dec){
	cout <<"Success" << "\n";  
	   }
   return 0;
}


