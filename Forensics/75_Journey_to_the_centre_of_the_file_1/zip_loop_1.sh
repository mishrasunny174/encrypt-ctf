#!/bin/bash

rm -r tmp
mkdir tmp
cp flag.txt tmp/
cd tmp/
for i in {1..69}
do
	if [ $((i%2)) -eq 0 ]
   	then
   		zip -m flag.zip *
	else
		gzip -v *
   		mv * flag.gz
	fi
done