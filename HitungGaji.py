print("=========================================================")
print("PROGRAM HITUNG GAJI BULANAN KARYAWAN")
print("=========================================================")

ListPekerja = []
listPekerja.append(['NIP','Nama','Jabatan','Gaji Pokok','Tunjangan','Uang Lembur','Gaji Kotor',
                 'Asuransi','Pajak','Telat','Potongan','Gaji Bersih'])
Jabatan = ['Direktur','Manager','SPV','Staff','OB']
GajiPokok = [7000000,5000000,3000000,20000000,1000000]
Tunjangan = [3000000,2000000,1500000,1000000,500000]
UpahLembur =  
upahlemburtanggalmerah = 
PajakGajiPokok = 5 % #dari gaji pokok
DendaKeterlambatan = 25000

print('No.','\t','Jabatan','\t','Gaji Pokok','\t','Tunjangan')
for i in range(3):
    print(i+1,'\t',jabatan[i],'\t',gajipokok[i],'\t',tunjangan[i])

totalkaryawan  = int(input('jumlah total karyawan dalam perusahaan : ')
                     
for i in (totalkaryawan+1):
    data = []
    #datanya = (data) 
    nama = input('Nama Karyawan : ')
    NIP = input('Nomor Induk Pegawai : ')
    jbt = int(input('Nomor jabatan : '))
    data.append(NIP)
    data.append(nama)
    data.append(jabatan[jbt-1])
    if jbt == 1:
        c = float(input('Banyak cuti : '))
        l = int(input('Banyaknya jam lembur : '))
        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
        t = int(input('Banyaknya jam keterlambatan : '))
        if c <= 2:
            gpk = gajipokok[0]
        else:
            gpk = gajipokok[0] - (c-2)*gajipokok[0]/25
        lemburan = l * lembur + merah * lemburtglmrh
        gajikotor = gpk + tunjangan[0] + lemburan
        asuransi = 0.02 * gpk
        pajak = pajakgm * gpk
        telat = t * dendatelat
        potongan = telat + asuransi + pajak
        gajibersih = gajikotor - potongan
        data.append(gpk)
        data.append(tunjangan[0])
        data.append(lemburan)
        data.append(gajikotor)
        data.append(asuransi)
        data.append(pajak)
        data.append(telat)
        data.append(potongan)
        data.append(gajibersih)
        dtkaryawan[nama] = data
        listpekerja.append(data)
    elif jbt == 2:
        c = float(input('Banyak cuti : '))
        l = int(input('Banyaknya jam lembur : '))
        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
        t = int(input('Banyaknya jam keterlambatan : '))
        if c <= 2:
            gpk = gajipokok[1]
        else:
            gpk = gajipokok[1] - (c-2)*gajipokok[1]/25
        lemburan = l * lembur + merah * lemburtglmrh
        gajikotor = gpk + tunjangan[1] + lemburan
        asuransi = 0.02 * gpk
        pajak = pajakgm * gpk
        telat = t * dendatelat
        potongan = telat + asuransi + pajak
        gajibersih = gajikotor - potongan
        data.append(gpk)
        data.append(tunjangan[1])
        data.append(lemburan)
        data.append(gajikotor)
        data.append(asuransi)
        data.append(pajak)
        data.append(telat)
        data.append(potongan)
        data.append(gajibersih)
        dtkaryawan[nama] = data
        listpekerja.append(data)
    elif jbt == 3:
        c = float(input('Banyak cuti : '))
        l = int(input('Banyaknya jam lembur : '))
        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
        t = int(input('Banyaknya jam keterlambatan : '))
        if c <= 2:
            gpk = gajipokok[2]
        else:
            gpk = gajipokok[2] - (c-2)*gajipokok[2]/25
        lemburan = l * lembur + merah * lemburtglmrh
        gajikotor = gpk + tunjangan[2] + lemburan
        asuransi = 0.02 * gpk
        pajak = pajakgm * gpk
        telat = t * dendatelat
        potongan = telat + asuransi + pajak
        gajibersih = gajikotor - potongan
        data.append(gpk)
        data.append(tunjangan[2])
        data.append(lemburan)
        data.append(gajikotor)
        data.append(asuransi)
        data.append(pajak)
        data.append(telat)
        data.append(potongan)
        data.append(gajibersih)
        dtkaryawan[nama] = data
        listpekerja.append(data)
     elif jbt == 4:
        c = float(input('Banyak cuti : '))
        l = int(input('Banyaknya jam lembur : '))
        merah = int(input('Banyaknya masuk di tanggal merah atau hari Minggu : '))
        t = int(input('Banyaknya jam keterlambatan : '))
        if c <= 2:
            gpk = gajipokok[3]
        else:
            gpk = gajipokok[3] - (c-2)*gajipokok[3]/25
        lemburan = l * lembur + merah * lemburtglmrh
        gajikotor = gpk + tunjangan[3] + lemburan
        asuransi = 0.02 * gpk
        pajak = pajakgm * gpk
        telat = t * dendatelat
        potongan = telat + asuransi + pajak
        gajibersih = gajikotor - potongan
        data.append(gpk)
        data.append(tunjangan[3])
        data.append(lemburan)
        data.append(gajikotor)
        data.append(asuransi)
        data.append(pajak)
        data.append(telat)
        data.append(potongan)
        data.append(gajibersih)
        dtkaryawan[nama] = data
        listpekerja.append(data)
    else:
        print('data tidak terdeteksi')
for gaji in listpekerja:
        print(gaji[0],'\t',gaji[1],'\t',gaji[2],'\t',gaji[3],'\t',gaji[4],'\t',gaji[5]gaji[6],'\t',gaji[7],'\t',gaji[8],'\t',gaji[9],'\t',gaji[10],'\t',gaji[11])
  
