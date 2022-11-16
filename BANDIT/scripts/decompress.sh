#!/bin/bash

# Recurso obtenido de S4vitar.

xxd -r data.txt > data

name_compressed=$(7z l data | grep "Name" -A 2 | tail -n 1 | awk 'NF{print $NF}')
7z x data > /dev/null 2>&1

while true; do
	7z l $name_compressed > /dev/null 2>&1
	
	if [ "$(echo $?)" == "0" ];then
		decompressed_next=$(7z l $name_compressed | grep "Name" -A 2 | tail -n 1 | awk 'NF{print $NF}')
		7z x $name_compressed > /dev/null 2>&1 && name_compressed=$decompressed_next
	else
		cat $name_compressed | awk '{print $4}'; rm data* 2>/dev/null
		exit 1
	fi
done
