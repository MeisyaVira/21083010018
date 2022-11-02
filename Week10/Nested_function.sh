#!/bin/bash

# Mendeklarasikan Fungsi
nama() {
     echo "Siapa namamu?"
     read nama
     npm # Memanggil Fungsi di Dalam Fungsi (fungsi bersarang)
}
npm() {
    echo "Sebutkan npm mu"
    read npm
    echo -e "Hai $nama dengan npm $npm, selamat datang \n di praktikum sistem operasi yang seru ini ya!"
}

# Memanggil Fungsi
nama
