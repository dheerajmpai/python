from numpy import append
from fractions import gcd
mod_array = [];
start_website = 1
end_website = 4000
#~ num_websites = 200
for i in range(start_website,end_website):
	file_name = str(i) + '.txt'
	with open("open_ssl_mod/"+file_name, 'r') as myfile:
		data=myfile.read().replace('\n', '')
	if data != '':
		data = data.replace("Public-Key: (2048 bit)Modulus:","0x")
		data = data.replace("Public-Key: (1024 bit)Modulus:","0x")
		data = data.replace("Public-Key: (4096 bit)Modulus:","0x")
		data = data.replace("Exponent: 65537 (0x10001)","")
		data = data.replace(":","")
		data = data.replace(" ","")
	
		n = int(data, 16);
		#~ print (n)
		mod_array.append(n);
from operator import mul
mod_array = list(set(mod_array))
mult_1 = reduce(mul, mod_array[:end_website/2:]);
mult_2 = reduce(mul, mod_array[end_website/2::]);
d = gcd(mult_1,mult_2)
print (d)
print mult_1

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
