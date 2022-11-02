#!/bin/bash

#Mendeklarasikan fungsi
panjang() {
echo "Masukkan panjang: "
read panjang
}
lebar() {
echo "Masukkan lebar: "
read lebar
}
luas() {
echo "Luas persegi: "
let luas=$panjang*$lebar
echo "$luas"
}

# Memanggil fungsi
panjang
lebar
luas
