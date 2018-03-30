from numpy import append
from fractions import gcd
mod_array = [];
num_websites = 4
for i in range(1,num_websites+1):
	file_name = str(i) + '.txt'
	with open(file_name, 'r') as myfile:
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
from numpy import size
arr_size = size(mod_array)
for j in range(arr_size):
	for k in range(j+1,arr_size):
		d = gcd(mod_array[j],mod_array[k])
		if d != 1:
			print (d)
			print (mod_array[j])
			if d != mod_array[j]:
				print "prime found"
				print (d)
				print (j)
				print (k)
				print "----d,j,k-----"
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
