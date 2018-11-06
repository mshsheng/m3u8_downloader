#!/bin/bash

read -p "Please input the number of .ts file:" num
#read -p "IV:" iv
read -p "Key:" key

#num=10
iv=00000000000000000000000000000000
#key=D2977D03339A8C7AA7FC44400150F9DF

for ((i=1;i<=num;i++));do
openssl aes-128-cbc -d -in v$i.ts -out $i.ts -nosalt -iv $iv -K $key
echo $i
done
