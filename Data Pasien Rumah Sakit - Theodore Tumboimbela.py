List_Pasien =[['1A','Adi Budidaya',12,'L','O'],
              ['1B','Sam Ratulangi',21,'P','A'],
              ['1C','Alex Papaya',16,'L','AB']] 


def main():                                                             
    print('==================Data Pasien Rumah Sakit==================')
    print('Pilih menu yang diinginkan')
    print('1. Tampilkan Data Pasien\n2. Tambahkan Pasien Baru\n3. Update Pasien\n4. Keluarkan Pasien\n5. Keluar Program')
    x = input('')
    if x.isnumeric() == False:              # Ulang jika memasuki value selain integer
        print('Inputkan sebuah angka')
        main()
    elif int(x) == 1:                     # Menuju Data Pasien
        DataPasien()
        
        
    elif int(x) == 2:                    # Menuju Penambahan Pasien
        TambahPasien()
        

    elif int(x) == 3:                      # Menuju Update Pasien
        UpdatePasien()
        
    elif int(x) == 4:                     # Menuju Pengurangan Pasien
        KurangPasien()
        
    elif int(x) == 5:                       # Mengakhiri Program
        print('Terima kasih')       
    else:
        print('Masukan angka antara 1-5')   # Ulang bila memasuki value 0 atau lebih dari 5
        main()

        
def DataPasien():
        print('==================Data Pasien ==================')

        print('1. Tampilkan Seluruh Data Pasien\n2. Tampilkan Data Pasien Tertentu\n3. Kembali ke Menu Utama')
        x = input('')
        if x.isnumeric() == False:
            print('Inputkan sebuah angka')
            DataPasien()
                
        elif int(x) == 1:                    # Seluruh Data Pasien
            listPasien()
            DataPasien()
                
        elif int(x) == 2:                    # Data Pasien Tertentu
            listPasienTertentu()          
            DataPasien()
            
        elif int(x) == 3:                     # Kembali ke Menu Utama
            main()

        
def listPasien():
    print('=======================List Pasien=======================')
    if List_Pasien != []:
        print('NIP\t|Nama\t\t|Umur\t|Gender\t|Golongan Darah')
        for i in range  (len(List_Pasien)):
            print(f'{List_Pasien[i][0]}\t| {List_Pasien[i][1]}\t| {List_Pasien[i][2]}\t| {List_Pasien[i][3]}\t| {List_Pasien[i][4]}')
    else:
        print('Data kosong')
        DataPasien()

def listPasienTertentu():
    if List_Pasien != []:
        NIP = input('Masukan NIP Pasien tertentu:')
        print('==================List Pasien==================')

        if any(NIP in x for x in List_Pasien):
            list_no = 0
            pos = 0
            for i in range(0,len(List_Pasien)):
                try:
                    pos = List_Pasien[i].index(NIP)
                    break
                except:
                    pass
            print('NIP\t|Nama\t\t|Umur\t|Gender\t|Golongan Darah')
            print(f'{List_Pasien[i][0]}\t| {List_Pasien[i][1]}\t| {List_Pasien[i][2]}\t| {List_Pasien[i][3]}\t| {List_Pasien[i][4]}')    
        else:
            print('NIP tidak terdaftar')
            
    else:
        print('==================List Pasien==================')
        print('Data kosong')
        DataPasien()
    
    DataPasien()


def TambahPasien():
    print('==================Penambahan Data Pasien ==================')
    print('1. Tambah Data Pasien\n2. Kembali ke menu utama')
    o = int(input(''))
    if o == 1:
        while True:                                     # Untuk memeriksa apabila no NIP sudah terdaftar
            NIP = str(input('Masukan NIP:'))
            if any(NIP in x for x in List_Pasien):
                print('Nomor NIP sudah terdaftar')

            else:
                break

        z = input('Masukan nama pasien:')
        namaPasien = z.title()

        umurPasien = int(input('Masukan umur pasien:'))

        x = input('Masukan gender pasien ([L]Laki-laki [P]Perempuan):')
        genderPasien = x.upper()

        y = input('Masukan golongan darah pasien:')
        golDarahPasien = y.upper()

        c = input('Apakah data ingin disimpan(Y/N):')                                       # Menu tambahan untuk konfirmasi simpan data atau tidak
        if c.upper() == 'Y':
            List_Pasien.append([NIP,namaPasien,umurPasien,genderPasien,golDarahPasien])
            print('Data tersimpan')
            TambahPasien()
        elif c.upper() == 'N':
            listPasien()

    elif o == 2:
        main()


def UpdatePasien():
    print('==================Update Data Pasien ==================')
    print('')
    listPasien()
    print('1. Update Data Pasien\n2. Kembali ke menu utama')
    o = int(input(''))
    if o == 1:
        NIP = input('Masukan NIP Pasien tertentu:')         # Konfirmasi NIP
        if any(NIP in y for y in List_Pasien):
            list_no = 0
            pos = 0
            for i in range(0,len(List_Pasien)):
                try:
                    pos = List_Pasien[i].index(NIP)
                    break
                except:
                    pass

            print('NIP\t|Nama\t\t|Umur\t|Gender\t|Golongan Darah')
            print(f'{List_Pasien[i][0]}\t| {List_Pasien[i][1]}\t| {List_Pasien[i][2]}\t| {List_Pasien[i][3]}\t| {List_Pasien[i][4]}') 
            
            print('1. Nama\n2. Umur\n3. Gender\n4. Golongan Darah') 
            x = input(('Pilih data yang ingin diupdate:'))          # Menu untuk memilih data yang ingin di update

            if int(x) == 1:       #Nama
                a = input('Masukan nama baru:')
                List_Pasien[i][1] = a
            elif int(x) == 2:       #Umur
                b = input('Masukan nama baru:')
                List_Pasien[i][2] = b
            
            elif int(x) == 3:       #Gender
                c = input('Masukan nama baru:')
                List_Pasien[i][3] = c
            elif int(x) == 4:       #Golongan Darah
                d = input('Masukan nama baru:')
                List_Pasien[i][4] = d
            UpdatePasien()        
        else:
            print('NIP tidak terdaftar')  
            UpdatePasien()  
    elif o == 2:
        main()

def KurangPasien():
    print('==================Pengeluaran Data Pasien ==================')
    listPasien()
    print('1. Hapus Data Pasien\n2. Kembali ke menu utama')
    o = int(input(''))
    if o == 1:
        while True:                                                         # Menuju Data Pasien
            NIP = str(input('Masukan NIP pasien yang ingin dikeluarkan:'))
            if any(NIP in x for x in List_Pasien):
                break

            else:
                print('Nomor NIP tidak terdaftar')
        list_no = 0
        pos = 0
        for i in range(0,len(List_Pasien)):
            try:
                pos = List_Pasien[i].index(NIP)
                break
            except:
                pass
        List_Pasien.pop(i)
        listPasien()
        KurangPasien()
    elif o == 2:
        main()

    
main()
