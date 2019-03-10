#!/bin/bash

cd tmp/
for i in {1..69}
do
	if [ $((i%2)) -eq 0 ]
   	then
   		gzip -d *
	else
		unzip *
		rm *.zip > /dev/null 2>&1
	fi
done