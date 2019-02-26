#!/bin/bash

cd tmp/
filename=$(ls)
rm -r tmp2/
mkdir tmp2/
cp $filename tmp2/
cd tmp2/
filename=$(ls)
while [ 1 ]
do
	file $filename
	file $filename | grep "bzip2"
	if [ "$?" -eq 0 ]
	then
		mv $filename $filename.bz2
		bunzip2 $filename.bz2 > /dev/null
		filename=$(ls)	
	fi

	file $filename | grep "Zip"
	if [ "$?" -eq 0 ]
	then
		mv $filename $filename.zip
		unzip $filename.zip > /dev/null
		rm $filename.zip > /dev/null 2>&1
		filename=$(ls)	
	fi

	file $filename | grep "gzip"
	if [ "$?" -eq 0 ]
	then
		mv $filename $filename.gz
		gunzip $filename.gz > /dev/null
		filename=$(ls)
	fi

	file $filename | grep "ASCII"
	if [ "$?" -eq 0 ]
	then
		echo 
		echo
		echo "Flag Found!"
		echo
		cat $filename
		echo
		echo
		break
	fi
done
