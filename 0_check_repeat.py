from numpy import append
from fractions import gcd
from numpy import where
prime_array = [];
start_website = 1
end_website = 50000
#~ num_websites = 200
for i in range(start_website,end_website):
	#~ file_name = str(i) + '.pem'
	file_name = "OpenSSL_trial/PRIMES/"+str(i) + '.txt'
	with open(file_name, 'r') as myfile:
		data=myfile.readlines()
	#~ print data
	#~ print data[40]
	#~ print data[50]
	#~ print data[60]
	prime_1 = "".join(data[41:50]).replace(":","")
	prime_1 = prime_1.replace("\n","")
	prime_1 = prime_1.replace(" ","")
	prime_2 = "".join(data[51:60]).replace(":","")
	prime_2 = prime_2.replace("\n","")
	prime_2 = prime_2.replace(" ","")
	
	print prime_1	
	print prime_2
	prime_array.append(prime_1)
	prime_array.append(prime_2)
	
mod_array = list(set(prime_array))
#~ print prime_array
from numpy import size
print size(prime_array)
print size(mod_array)
		#~ print where(data == data[1])
		#~ print (data[41])
		#~ data = data.replace("Public-Key: (2048 bit)Modulus:","0x")
		#~ data = data.replace("Public-Key: (1024 bit)Modulus:","0x")
		#~ data = data.replace("Public-Key: (4096 bit)Modulus:","0x")
		#~ data = data.replace("Exponent: 65537 (0x10001)","")
		#~ data = data.replace(":","")
		#~ data = data.replace(" ","")
	#~ 
		#~ n = int(data, 16);
		#~ print (n)
		#~ mod_array.append(n);
#~ from operator import mul
#~ mod_array = list(set(mod_array))
#~ mult_1 = reduce(mul, mod_array[:end_website/2:]);
#~ mult_2 = reduce(mul, mod_array[end_website/2::]);
#~ d = gcd(mult_1,mult_2)
#~ print (d)
#~ print mult_1

#~ from numpy import size
#~ arr_size = size(mod_array)
#~ print (arr_size)
#~ for j in range(arr_size):
	#~ for k in range(j,arr_size):
		#~ d = gcd(mod_array[j],mod_array[k])
		#~ if d != 1:
			#print (d)
			#print (mod_array[j])
			#~ if d != mod_array[j]:
				#~ print "prime found"
				#~ print (d)
				#~ print (j)
				#~ print (k)
				#~ print "----d,j,k-----"
#~ for i in range(1,47):
#~ file_name = '11' + '.txt'
#~ with open(file_name, 'r') as myfile:
	#~ data=myfile.read().replace('\n', '')
#~ 
#~ data = data.replace("Public-Key: (2048 bit)Modulus:","0x")
#~ data = data.replace("Exponent: 65537 (0x10001)","")
#~ data = data.replace(":","")
#~ data = data.replace(" ","")
#~ 
#~ n = int(data, 16);
#~ mod_array.append(n);
