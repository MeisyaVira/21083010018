#!/bin/bash

# Mendeklarasikan Fungsi
identifikasi() {
    parameter1=$1
    parameter2=$2
    parameter3=$3
    echo "$parameter1"
    echo "$parameter2"
    echo "$parameter3"
}

echo "Masukkan Nama : "
read a
echo "Masukkan Npm : "
read b
echo "Hobimu Apa : "
read c

printf "\n"
identifikasi $a $b $c
