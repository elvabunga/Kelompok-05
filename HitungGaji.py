import csv
from os import system
import time

listPekerja = []
listPekerja.append(['NIP','Nama','Jabatan','Gaji Pokok','Tunjangan','Upah Lembur','Gaji Kotor','Asuransi','Pajak   ','Telat','Potongan','Gaji Bersih'])
Jabatan = ['Direktur','Manager','Supervisor','Staff ','Janitor']
GajiPokok = [7000000,5000000,3000000,2000000,1000000]
Tunjangan = [3000000,2000000,1500000,1000000,500000]
PajakGajiPokok = 0.05 #dari gaji pokok
DendaKeterlambatan = 25000
lembur=25000
lemburtglmrh=100000
isinyadata=len(Jabatan)

def header():
    print("===================INFORMASI JABATAN, GAJI POKOK, DAN TUNJANGAN===================")
    print()
    print('No.','\t','Jabatan','\t','Gaji Pokok','\t','Tunjangan')
    for i in range(isinyadata):
        print(i+1,'\t',Jabatan[i],'\t',GajiPokok[i],'\t',Tunjangan[i])

def proses():
    totalkaryawan= int(input('jumlah total karyawan dalam perusahaan : '))
                         
    for i in range (totalkaryawan):
        data = []
        #datanya = (data) 
        nama = input('Nama Karyawan : ')
        NIP = input('Nomor Induk Pegawai : ')
        jbt = int(input('Nomor Jabatan : '))
        data.append(NIP)
        data.append(nama)
        data.append(Jabatan[jbt-1])
        if jbt == 1:
            c = float(input('Banyak cuti : '))
            l = int(input('Banyaknya jam lembur : '))
            merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
            t = int(input('Banyaknya jam keterlambatan : '))
            if c <= 2:
                gpk = GajiPokok[0]
            else:
                gpk = GajiPokok[0] - (c-2)*GajiPokok[0]/25
            lemburan = l * lembur + merah * lemburtglmrh
            gajikotor = gpk + Tunjangan[0] + lemburan
            asuransi = 0.02 * gpk
            pajak = PajakGajiPokok * gpk
            telat = t * DendaKeterlambatan
            potongan = telat + asuransi + pajak
            gajibersih = gajikotor - potongan
            data.append(gpk)
            data.append(Tunjangan[0])
            data.append(lemburan)
            data.append(gajikotor)
            data.append(asuransi)
            data.append(pajak)
            data.append(telat)
            data.append(potongan)
            data.append(gajibersih)
            listPekerja.append(data)
        elif jbt == 2:
            c = float(input('Banyak cuti : '))
            l = int(input('Banyaknya jam lembur : '))
            merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
            t = int(input('Banyaknya jam keterlambatan : '))
            if c <= 2:
                gpk = GajiPokok[1]
            else:
                gpk = GajiPokok[1] - (c-2)*GajiPokok[1]/25
            lemburan = l * lembur + merah * lemburtglmrh
            gajikotor = gpk + Tunjangan[1] + lemburan
            asuransi = 0.02 * gpk
            pajak = PajakGajiPokok * gpk
            telat = t * DendaKeterlambatan
            potongan = telat + asuransi + pajak
            gajibersih = gajikotor - potongan
            data.append(gpk)
            data.append(Tunjangan[1])
            data.append(lemburan)
            data.append(gajikotor)
            data.append(asuransi)
            data.append(pajak)
            data.append(telat)
            data.append(potongan)
            data.append(gajibersih)
            listPekerja.append(data)
        elif jbt == 3:
            c = float(input('Banyak cuti : '))
            l = int(input('Banyaknya jam lembur : '))
            merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
            t = int(input('Banyaknya jam keterlambatan : '))
            if c <= 2:
                gpk = GajiPokok[2]
            else:
                gpk = GajiPokok[2] - (c-2)*GajiPokok[2]/25
            lemburan = l * lembur + merah * lemburtglmrh
            gajikotor = gpk + Tunjangan[2] + lemburan
            asuransi = 0.02 * gpk
            pajak = PajakGajiPokok * gpk
            telat = t * DendaKeterlambatan
            potongan = telat + asuransi + pajak
            gajibersih = gajikotor - potongan
            data.append(gpk)
            data.append(Tunjangan[2])
            data.append(lemburan)
            data.append(gajikotor)
            data.append(asuransi)
            data.append(pajak)
            data.append(telat)
            data.append(potongan)
            data.append(gajibersih)
            listPekerja.append(data)
        elif jbt == 4:
            c = float(input('Banyak cuti : '))
            l = int(input('Banyaknya jam lembur : '))
            merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
            t = int(input('Banyaknya jam keterlambatan : '))
            if c <= 2:
                gpk = GajiPokok[3]
            else:
                gpk = GajiPokok[3] - (c-2)*GajiPokok[3]/25
            lemburan = l * lembur + merah * lemburtglmrh
            gajikotor = gpk + Tunjangan[3] + lemburan
            asuransi = 0.02 * gpk
            pajak = PajakGajiPokok * gpk
            telat = t * DendaKeterlambatan
            potongan = telat + asuransi + pajak
            gajibersih = gajikotor - potongan
            data.append(gpk)
            data.append(Tunjangan[3])
            data.append(lemburan)
            data.append(gajikotor)
            data.append(asuransi)
            data.append(pajak)
            data.append(telat)
            data.append(potongan)
            data.append(gajibersih)
            listPekerja.append(data)
        elif jbt == 5:
            c = float(input('Banyak cuti : '))
            l = int(input('Banyaknya jam lembur : '))
            merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
            t = int(input('Banyaknya jam keterlambatan : '))
            if c <= 2:
                gpk = GajiPokok[4]
            else:
                gpk = GajiPokok[4] - (c-2)*GajiPokok[4]/25
            lemburan = l * lembur + merah * lemburtglmrh
            gajikotor = gpk + Tunjangan[4] + lemburan
            asuransi = 0.02 * gpk
            pajak = PajakGajiPokok * gpk
            telat = t * DendaKeterlambatan
            potongan = telat + asuransi + pajak
            gajibersih = gajikotor - potongan
            data.append(gpk)
            data.append(Tunjangan[4])
            data.append(lemburan)
            data.append(gajikotor)
            data.append(asuransi)
            data.append(pajak)
            data.append(telat)
            data.append(potongan)
            data.append(gajibersih)
            listPekerja.append(data)
        else:
            print('data tidak terdeteksi')
    system('cls')
    for gaji in listPekerja:
            print(gaji[0],'\t',gaji[1],'\t',gaji[2],'\t',gaji[3],'\t',gaji[4],'\t',gaji[5],
                  '\t',gaji[6],'\t',gaji[7],'\t',gaji[8],'\t',gaji[9],'\t',gaji[10],'\t',gaji[11])



def nuliskeCSV():
    namafile=input("Inputkan nama file (format : NAMAFILE.csv) : ")
    with open(namafile, 'w', newline='') as csvfile:
       
        fieldnames = ['NIP','Nama','Jabatan','Gaji Pokok', 'Tunjangan', 'Upah Lembur', 
                      'Gaji Kotor', 'Asuransi', 'Pajak', 'Telat', 'Potongan', 'Gaji Bersih']
    
        thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
       
        for gaji in listPekerja:
            thewriter.writerow({'NIP':gaji[0],'Nama':gaji[1], 'Jabatan':gaji[2], 
                                'Gaji Pokok':gaji[3], 'Tunjangan':gaji[4], 
                                'Upah Lembur':gaji[5], 'Gaji Kotor':gaji[6], 
                                'Asuransi':gaji[7], 'Pajak':gaji[8], 
                                'Telat':gaji[9], 'Potongan':gaji[10], 
                                'Gaji Bersih':gaji[11]})

print("=======================================================================")
print("                      PROGRAM PENGGAJIAN KARYAWAN")
print("                              P.T.EXODUS")
print("             Jl. Jalan Sama Kamu 2019 A telp : (0271)783193")
print("=======================================================================")
time.sleep(1)
print()
print("PLEASE WAIT.....")
time.sleep(3)
system('cls')

header()
proses()
while True:
    tanya=input("Apakah anda ingin mengexport data ke file CSV? (y/n) : ")
    if tanya =='y':
        nuliskeCSV()
        print("BERHASIL !")
        print("TERIMAKASIH")
        print()
        print("MENUTUP PROGRAM.....")
        time.sleep(2)
        break
    elif tanya =='n':
        print("TERIMAKASIH")
        print()
        print("MENUTUP PROGRAM.....")
        time.sleep(2)
        break
    else:
        print("INPUTAN TIDAK TERDETEKSI")
        time.sleep(1)
        system('cls')
