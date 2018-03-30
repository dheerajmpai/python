#include<NTL/ZZ_p.h>
#include <NTL/ZZ.h>
#include<NTL/ZZ_pXFactoring.h>
#include<NTL/vector.h>
using namespace std;
using namespace NTL;
//~ P=648293
//~ Q=848993
//~ N=550396218949

int main()
{
	//~ Vec<ZZ> v;
   ZZ n,p,q,f,n_cpy; 
   //~ n = 550396218949;
   long L = 25;
   //~ long l = L * 0.30102;
   //~ GenGermainPrime(p,L,800);
   //~ GenGermainPrime(q,L,800);
   //~ n = p*q;
   cin >> n;
   //~ add(n,n,ZZ(123045765651651846354896))
   //~ 072979014
   
   //~ n = 4104;
   n_cpy = n;
   //~ f=(p-1)*(q-1);
   cout <<"P="<< p << "\n";   cout <<"Q="<< q << "\n";
   cout <<"N="<< n << "\n";
   ZZ c;
   SqrRoot(c,n);
   //~ power(c,2,L*2);
   //~ c = power(10,L);
   cout <<"c="<< c << "\n";
   ZZ i;
   ZZ t;
   t = 1;
   for (i=2;i<c;i++){
	   //~ cout <<"i = " << i << "\n";
	   if(divide(n,i)){
		   cout <<"P="<< i << "\n";
		   div(n, n, i);
		   t = t*i;
		   }
		if(n == 1){
			break;
			}
	   }
	t = t*n;
	cout <<"P="<< n << "\n";
	cout <<"DONE " << "\n";
	cout <<"VERIFY " << t << "\n";
	if (n_cpy == t){
		cout <<"Verification Successfull " << "\n";
		}
	//~ cout << 
   return 0;
}



