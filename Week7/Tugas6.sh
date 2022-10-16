#!/bin/bash

echo -n "input total semester terlebih dahulu kemudian IPS: "
read semester

declare -a IPS

i=0
let jumlah=$semester-1

while [ $i -le $jumlah ];
do
	let nilai=$i+1
	printf " " $nilai;
	read nilaisem;
	IPS[$i]=$nilaisem;
	let total=total+$nilaisem;
	let i=$i+1;
done

let IPK=$total/$semester
echo "jumlah IPS mhs = " $total
echo "IPK mhs = " $IPK
