#!/bin/bash

echo "1. Ganjil";
echo "2. Genap";
echo -n "Pilih "
read pil
if [ $pil -eq 1 ];
then
i=1;
echo -n "Masukkan angka: "
read x
while [ $x -gt 0 ]
do
  echo $x
  x=$((x - 2))
done
elif [ $pil -eq 2 ];
then
i=1;
echo -n "Masukkan angka: "
read x
until [ $i -gt $x ];
do
echo -n $i " ";
let i=$i+2
done
fi
