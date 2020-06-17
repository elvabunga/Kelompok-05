import csv
from os import system
import time
print("=======================================================================")
print("                      PROGRAM PENGGAJIAN KARYAWAN")
print("                              P.T.EXODUS")
print("             Jl. Jalan Sama Kamu 2019 A telp : (0271)783193")
print("=======================================================================")
time.sleep(1)
print()
print("PLEASE WAIT.....")
time.sleep(3)

print()
while True:
    print('Menu : ')
    print('1. Update Standar Gaji Karyawan')
    print('2. Menghitung gaji karyawan')
    print('3. Menampilkan data gaji karyawan')
    print('4. Quit')
    print()
    
    try:
        a = int(input('Pilih menu yang akan digunakan : '))
        system('cls')
    except ValueError as ve:
        print(ve)
        print('Inputkan angka pada menu yang ingin digunakan')
        exit()
    
    listPekerja = []
    listPekerja.append(['NIP','Nama','Jabatan','Gaji Pokok','Tunjangan','Upah Lembur','Gaji Kotor','Asuransi','Pajak   ','Telat','Potongan','Gaji Bersih'])
    Jabatan = ['Direktur','Manager','Supervisor','Staff ','Janitor']
    GajiPokok = [7000000,5000000,3000000,2000000,1000000]
    Tunjangan = [3000000,2000000,1500000,1000000,500000]
    PajakGajiPokok = 0.1 #dari gaji pokok
    DendaKeterlambatan = 2000
    lembur= 50000
    lemburtglmrh= 300000
    isinyadata=len(Jabatan)
        
    if a == 1: 
        print("===================PERTANYAAN PENDAHULUAN===================")
        print('List jabatan')
        for i in range(len(Jabatan)):
            print(i+1, Jabatan[i])
        listPekerja.append(['NIP','Nama','Jabatan','Gaji Pokok','Tunjangan','Upah Lembur','Gaji Kotor','Asuransi','Pajak   ','Telat','Potongan','Gaji Bersih'])
        Jabatan = ['Direktur','Manager','Supervisor','Staff ','Janitor']
        GajiPokokU = []
        TunjanganU = []

        isinyadata=len(Jabatan)
        try:
            gajipokok1 = int(input('Input gaji pokok bulanan Direktur : '))
            GajiPokokU.append(gajipokok1)
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            gajipokok2 = int(input('Input gaji pokok bulanan Manager : '))
            GajiPokokU.append(gajipokok2)
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            gajipokok3 = int(input('Input gaji pokok bulanan Supervisor : '))
            GajiPokokU.append(gajipokok3)
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            gajipokok4 = int(input('Input gaji pokok bulanan Staff : '))
            GajiPokokU.append(gajipokok4)
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            gajipokok5 = int(input('Input gaji pokok bulanan Janitor : '))
            GajiPokokU.append(gajipokok5)
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            tunjangan1 = int(input('Input Tunjangan Direktur : '))
            TunjanganU.append(tunjangan1)
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            tunjangan2 = int(input('Input Tunjangan Manager : '))
            TunjanganU.append(tunjangan2)
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            tunjangan3 = int(input('Input Tunjangan Supervisor : '))
            TunjanganU.append(tunjangan3)
        except ValueError  as ve:
            print(ValueError)
            time.sleep(2)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            tunjangan4 = int(input('Input Tunjangan Staff : '))
            TunjanganU.append(tunjangan4)
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            tunjangan5 = int(input('Input Tunjangan Janitor : '))
            TunjanganU.append(tunjangan5)
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            PajakGajiPokokU = float(input('Inputkan pajak yang harus dibayar oleh setiap karyawan (dalam desimal kurang dari 1) : ')) #dari gaji pokok
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            DendaKeterlambatanU = int(input('Inputkan denda keterlambatan yang harus dibayar oleh karyawan setiap keterlambatan 1 menit : '))
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            lemburU = int(input('Input gaji lembur yang diterima karyawan per jamnya : '))
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
        try:
            lemburtglmrhU = int(input('Input gaji yang diterima karyawan setiap bekerja di tanggal merah : '))
        except ValueError as ve:
            print(ValueError)
            exit()
        except TypeError as te:
            print(TypeError)
            exit()
    
    elif a == 2:
        def header():
            print("===================INFORMASI JABATAN, GAJI POKOK, DAN TUNJANGAN===================")
            print()
            print('No.','\t','Jabatan','\t','Gaji Pokok','\t','Tunjangan')
            for i in range(isinyadata):
                print(i+1,'\t',Jabatan[i],'\t',GajiPokok[i],'\t',Tunjangan[i])
        def headerU():
            print("===================INFORMASI JABATAN, GAJI POKOK, DAN TUNJANGAN===================")
            print()
            print('No.','\t','Jabatan','\t','Gaji Pokok','\t','Tunjangan')
            for i in range(isinyadata):
                print(i+1,'\t',Jabatan[i],'\t',GajiPokokU[i],'\t',TunjanganU[i])
    
        def proses():
            Iterasi = True
    
            while Iterasi == True :
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
                    if c <= 2:
                        gpk = GajiPokok[0]
                    else:
                        gpk = GajiPokok[0] - (c-2)*GajiPokok[0]/25
                    try:
                        l = int(input('Banyaknya jam lembur : '))
                        lembur1 = l * lembur
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
                        lembur2 = merah * lemburtglmrh
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        t = int(input('Banyaknya menit keterlambatan : '))
                        telat = t * DendaKeterlambatan
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    lemburan =  lembur1 + lembur2
                    gajikotor = gpk + Tunjangan[0] + lemburan
                    asuransi = 0.02 * gpk
                    pajak = PajakGajiPokok * gpk
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
                    if c <= 2:
                        gpk = GajiPokok[1]
                    else:
                        gpk = GajiPokok[1] - (c-2)*GajiPokok[1]/25
                    try:
                        l = int(input('Banyaknya jam lembur : '))
                        lembur1 =l * lembur
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
                        lembur2 = merah * lemburtglmrh
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        t = int(input('Banyaknya menit keterlambatan : '))
                        telat = t * DendaKeterlambatan
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    lemburan =  lembur1 + lembur2
                    gajikotor = gpk + Tunjangan[1] + lemburan
                    asuransi = 0.02 * gpk
                    pajak = PajakGajiPokok * gpk
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
                    if c <= 2:
                        gpk = GajiPokok[2]
                    else:
                        gpk = GajiPokok[2] - (c-2)*GajiPokok[2]/25
                    try:
                        l = int(input('Banyaknya jam lembur : '))
                        lembur1 =l * lembur
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
                        lembur2 = merah * lemburtglmrh
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        t = int(input('Banyaknya menit keterlambatan : '))
                        telat = t * DendaKeterlambatan
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    lemburan =  lembur1 + lembur2
                    gajikotor = gpk + Tunjangan[2] + lemburan
                    asuransi = 0.02 * gpk
                    pajak = PajakGajiPokok * gpk
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
                    if c <= 2:
                        gpk = GajiPokok[3]
                    else:
                        gpk = GajiPokok[3] - (c-2)*GajiPokok[3]/25
                    try:
                        l = int(input('Banyaknya jam lembur : '))
                        lembur1 =l * lembur
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
                        lembur2 = merah * lemburtglmrh
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        t = int(input('Banyaknya menit keterlambatan : '))
                        telat = t * DendaKeterlambatan
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    lemburan =  lembur1 + lembur2
                    gajikotor = gpk + Tunjangan[3] + lemburan
                    asuransi = 0.02 * gpk
                    pajak = PajakGajiPokok * gpk
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
                    if c <= 2:
                        gpk = GajiPokok[4]
                    else:
                        gpk = GajiPokok[4] - (c-2)*GajiPokok[4]/25          
                    try:
                        l = int(input('Banyaknya jam lembur : '))
                        lembur1 = l * lembur
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
                        lembur2 = merah * lemburtglmrh
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        t = int(input('Banyaknya menit keterlambatan : '))
                        telat = t * DendaKeterlambatan
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    lemburan =  lembur1 + lembur2
                    gajikotor = gpk + Tunjangan[4] + lemburan
                    asuransi = 0.02 * gpk
                    pajak = PajakGajiPokok * gpk
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
    
                x = input('Ingin menambah data? (y/n) : ')
                if x != 'y':
                    Iterasi = False
    
            system('cls')
            for gaji in listPekerja:
                    print(gaji[0],'\t',gaji[1],'\t',gaji[2],'\t',gaji[3],'\t',gaji[4],'\t',gaji[5],
                          '\t',gaji[6],'\t',gaji[7],'\t',gaji[8],'\t',gaji[9],'\t',gaji[10],'\t',gaji[11])
    
            print('Jumlah Karyawan : ', len(listPekerja)-1)
            
        def prosesU():
            Iterasi = True
    
            while Iterasi == True :
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
                    if c <= 2:
                        gpk = GajiPokokU[0]
                    else:
                        gpk = GajiPokokU[0] - (c-2)*GajiPokokU[0]/25
                    try:
                        l = int(input('Banyaknya jam lembur : '))
                        lembur1 = l * lemburU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
                        lembur2 = merah * lemburtglmrhU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        t = int(input('Banyaknya menit keterlambatan : '))
                        telat = t * DendaKeterlambatanU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    lemburan =  lembur1 + lembur2
                    gajikotor = gpk + TunjanganU[0] + lemburan
                    asuransi = 0.02 * gpk
                    pajak = PajakGajiPokokU * gpk
                    potongan = telat + asuransi + pajak
                    gajibersih = gajikotor - potongan
                    data.append(gpk)
                    data.append(TunjanganU[0])
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
                    if c <= 2:
                        gpk = GajiPokokU[1]
                    else:
                        gpk = GajiPokokU[1] - (c-2)*GajiPokokU[1]/25
                    try:
                        l = int(input('Banyaknya jam lembur : '))
                        lembur1 =l * lemburU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
                        lembur2 = merah * lemburtglmrhU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        t = int(input('Banyaknya menit keterlambatan : '))
                        telat = t * DendaKeterlambatanU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    lemburan =  lembur1 + lembur2
                    gajikotor = gpk + TunjanganU[1] + lemburan
                    asuransi = 0.02 * gpk
                    pajak = PajakGajiPokokU * gpk
                    potongan = telat + asuransi + pajak
                    gajibersih = gajikotor - potongan
                    data.append(gpk)
                    data.append(TunjanganU[1])
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
                    if c <= 2:
                        gpk = GajiPokokU[2]
                    else:
                        gpk = GajiPokokU[2] - (c-2)*GajiPokokU[2]/25
                    try:
                        l = int(input('Banyaknya jam lembur : '))
                        lembur1 =l * lemburU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
                        lembur2 = merah * lemburtglmrhU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        t = int(input('Banyaknya menit keterlambatan : '))
                        telat = t * DendaKeterlambatanU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    lemburan =  lembur1 + lembur2
                    gajikotor = gpk + TunjanganU[2] + lemburan
                    asuransi = 0.02 * gpk
                    pajak = PajakGajiPokokU * gpk
                    potongan = telat + asuransi + pajak
                    gajibersih = gajikotor - potongan
                    data.append(gpk)
                    data.append(TunjanganU[2])
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
                    if c <= 2:
                        gpk = GajiPokokU[3]
                    else:
                        gpk = GajiPokokU[3] - (c-2)*GajiPokokU[3]/25
                    try:
                        l = int(input('Banyaknya jam lembur : '))
                        lembur1 =l * lemburU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
                        lembur2 = merah * lemburtglmrhU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        t = int(input('Banyaknya menit keterlambatan : '))
                        telat = t * DendaKeterlambatanU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    lemburan =  lembur1 + lembur2
                    gajikotor = gpk + Tunjangan[3] + lemburan
                    asuransi = 0.02 * gpk
                    pajak = PajakGajiPokokU * gpk
                    potongan = telat + asuransi + pajak
                    gajibersih = gajikotor - potongan
                    data.append(gpk)
                    data.append(TunjanganU[3])
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
                    if c <= 2:
                        gpk = GajiPokokU[4]
                    else:
                        gpk = GajiPokokU[4] - (c-2)*GajiPokokU[4]/25          
                    try:
                        l = int(input('Banyaknya jam lembur : '))
                        lembur1 = l * lemburU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
                        lembur2 = merah * lemburtglmrhU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    try:
                        t = int(input('Banyaknya menit keterlambatan : '))
                        telat = t * DendaKeterlambatanU
                    except ValueError as ve:
                        print(ve)
                        time.sleep(1)
                        break
                    lemburan =  lembur1 + lembur2
                    gajikotor = gpk + TunjanganU[4] + lemburan
                    asuransi = 0.02 * gpk
                    pajak = PajakGajiPokokU * gpk
                    potongan = telat + asuransi + pajak
                    gajibersih = gajikotor - potongan
                    data.append(gpk)
                    data.append(TunjanganU[4])
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
    
                x = input('Ingin menambah data? (y/n) : ')
                if x != 'y':
                    Iterasi = False
    
            system('cls')
            for gaji in listPekerja:
                    print(gaji[0],'\t',gaji[1],'\t',gaji[2],'\t',gaji[3],'\t',gaji[4],'\t',gaji[5],
                          '\t',gaji[6],'\t',gaji[7],'\t',gaji[8],'\t',gaji[9],'\t',gaji[10],'\t',gaji[11])
    
            print('Jumlah Karyawan : ', len(listPekerja)-1)
    
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
    
        

        system('cls')
        d = input('apakah anda telah mengupdate standar penggajian?(y/n)')
        if d == 'y':
            b = input('apakah anda ingin menggunakan standar penggajian yang sudah di update?(y/n) : ')
            if b == 'y':
                headerU()
                prosesU()
                while True:
                    tanya=input("Apakah anda ingin mengexport data ke file CSV? (y/n) : ")
                    if tanya =='y':
                        nuliskeCSV()
                        print("BERHASIL !")
                        print("TERIMAKASIH")
                        print()
                        print("KEMBALI KE MENU AWAL.....")
                        time.sleep(2)
                        break
                    elif tanya =='n':
                        print("TERIMAKASIH")
                        print()
                        print("KEMBALI KE MENU AWAL.....")
                        time.sleep(2)
                        break
                    else:
                        print("INPUTAN TIDAK TERDETEKSI")
                        time.sleep(1)
                        system('cls')
            elif b == 'n':
                header()
                proses()
                while True:
                    tanya=input("Apakah anda ingin mengexport data ke file CSV? (y/n) : ")
                    if tanya =='y':
                        nuliskeCSV()
                        print("BERHASIL !")
                        print("TERIMAKASIH")
                        print()
                        print("KEMBALI KE MENU AWAL.....")
                        time.sleep(2)
                        break
                    elif tanya =='n':
                        print("TERIMAKASIH")
                        print()
                        print("KEMBALI KE MENU AWAL.....")
                        time.sleep(2)
                        break
                    else:
                        print("INPUTAN TIDAK TERDETEKSI")
                        time.sleep(1)
                        system('cls')
            else:
                print('Inputan tidak terdeteksi')
        elif d == 'n':
            header()
            proses()
            while True:
                tanya=input("Apakah anda ingin mengexport data ke file CSV? (y/n) : ")
                if tanya =='y':
                    nuliskeCSV()
                    print("BERHASIL !")
                    print("TERIMAKASIH")
                    print()
                    print("KEMBALI KE MENU AWAL.....")
                    time.sleep(2)
                    break
                elif tanya =='n':
                    print("TERIMAKASIH")
                    print()
                    print("KEMBALI KE MENU AWAL.....")
                    time.sleep(2)
                    break
                else:
                    print("INPUTAN TIDAK TERDETEKSI")
                    time.sleep(1)
                    system('cls')
        else:
           print('Inputan tidak terdeteksi')  
            
    elif a == 3:
        print('==================PEMBUKAAN DATA GAJI==================')
        try:
            filename = input('Inputkan nama data dengan format NamaFile.csv : ')
            ListPekerja = []
            with open(filename,'r') as csvfile:
                readCSV = csv.reader(csvfile, delimiter = ',')
                for karyawan in readCSV:
                    ListPekerja.append(karyawan)
                    print(karyawan[0],'\t',karyawan[1],'\t',karyawan[2],'\t',karyawan[3],'\t',karyawan[4],'\t',karyawan[5],
                          '\t',karyawan[6],'\t',karyawan[7],'\t',karyawan[8],'\t',karyawan[9],'\t',karyawan[10],'\t',karyawan[11])
                print("BERHASIL !")
                print("TERIMAKASIH")
                print()
                print("KEMBALI KE MENU AWAL.....")
                time.sleep(2)
        except Exception as e:
            print('Sepertinya anda salah memasukkan format nama file')
            time.sleep(1)
            exit()
    elif a == 4:
        print('Terimakasih')
        exit()
    else:
        print('Menu tudak tersedia')
        break
