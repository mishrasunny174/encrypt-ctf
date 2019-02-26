#!/bin/bash

rm -r tmp
mkdir tmp
cp flag.txt tmp/
cd tmp/
for i in {1..69}
do
	if [ $((i%2)) -eq 0 ]
   	then
   		zip -m flag *
   	elif [ $((i%3)) -eq 0 ]
   	then
   		bzip2 *
   		mv * flag
	else
		gzip -v *
   		mv * flag
	fi
done