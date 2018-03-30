#!/bin/bash

for i in {1..50000}; do 
	#~ echo "$i.txt";
	openssl rsa -in  private_keys_2048/"$i".pem -text -noout >> PRIMES/"$i".txt

	#~ openssl genrsa -out private_keys_2048/"$i".pem 2048 
	#~ openssl rsa -in private_keys_2048/"$i".pem -outform PEM -pubout -out public_keys_2048/"$i"
	#~ openssl rsa -noout -text  -in public_keys_2048/"$i" -pubin > open_ssl_mod/"$i".txt
done
