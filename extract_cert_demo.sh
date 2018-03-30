#!/bin/bash
array=("www.google.co.in" "www.facebook.com" "stackoverflow.com")
# 
for i in "${array[@]}"; do   # The quotes are necessary here
    openssl s_client -showcerts -connect "$i":443 </dev/null >> "$i".crt
    openssl x509 -in crt_"$i".crt  -noout -pubkey > pub_"$i"-public
    openssl rsa -noout -text  -in pub_"$i"-public -pubin > hex_"$i"-public-hex
done
