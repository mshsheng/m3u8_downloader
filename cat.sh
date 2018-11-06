#!/bin/bash

read -p "Please input the number of .ts file:" num

for ((i=1;i<=num;i++));do
cat $i'.ts' >> out.ts
echo $i
done
