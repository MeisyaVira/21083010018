#import library
from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

#function
def cetak(i):
    if (i+1)%2==0:
        print(i+1, "Genap - ID proses", getpid())
    else:
        print(i+1, "Ganjil - ID proses", getpid())
    sleep(1)

#input nilai
n = int(input("Masukkan angka batasan: "))

#sekuensial
sekuensial_awal = time()
print("Sekuensial")
for i in range(n):
    cetak(i)
sekuensial_akhir = time()

#multiprocessing.Process
kumpulan_proses = []
proses_awal = time()
print("multiprocessing.Process")
for i in range(n):
    p = Process(target = cetak, args = (i, ))
    kumpulan_proses.append(p)
    p.start()
for i in kumpulan_proses:
    p.join()
proses_akhir = time()

#multiprocessing.Pool
pool_awal = time()
pool = Pool()
print("multiprocessing.Pool")
pool.map(cetak, range(0,n))
pool.close()
pool_akhir = time()

#Perbandingan waktu eksekusi
print("Waktu eksekusi sekuensial: ", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process: ", proses_akhir - proses_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool: ", pool_awal - pool_akhir, "detik")
