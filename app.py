import random
mobil = [
    {
        'nama' : 'Ayla' ,
        'penyedia' : [{
            'nama' : "Nabil RentCar",
            'harga' : 250000,
            'plat' : ['B 123 ABC', 'B 630 UTK']
        },
        {
            'nama' : "Rakha RentCar",
            'harga' : 260000,
            'plat' : ['B 222 ABD']
        },
        {
            'nama' : "Dwitya RentCar",
            'harga' : 260000,
            'plat' : ['B 333 CCC']

        }],
        'ukuran' : 4,
        'transmisi' : 'Automatic' 
    },
    {
        'nama': 'Mobilio',
        'penyedia' : [{
            'nama' : "Nabil RentCar",
            'harga' : 350000,
            'plat' : ['B 555 FNC', 'B 345 DFE']
        },
        {
            'nama' : "Rakha RentCar",
            'harga' : 360000,
            'plat' : ['B 987 TSM', 'B 135 SEN']
        }],
        'ukuran' : 6,
        'transmisi' : 'Automatic'
    }
]

mobilSedangDirental = [
    {
        'nama' : 'Ayla',
        'penyedia' : {
            'nama' : "Bil's RentCar",
            'harga' : 200000,
            'plat' : 'D 567 PPP'
        },
        'ukuran' : 4,
        'transmisi' : 'Automatic' 
    },
    {
        'nama': 'Mobilio',
        'penyedia' : {
            'nama' : "Dwitya RentCar",
            'harga' : 200000,
            'plat' : 'D 965 MHW'
        },
        'ukuran' : 6,
        'transmisi' : 'Automatic'
    },
    {
        'nama': 'Pajero',
        'penyedia' : {
            'nama' : "Test RentCar",
            'harga' : 500000,
            'plat' : 'Y 824 JJK'
        },
        'ukuran' : 6,
        'transmisi' : 'Automatic'
    }
        
]

def read_validated_input(dtype, message):
    temp_input = None
    while temp_input is None:
        try:
            temp_input = dtype(input(f"{message}"))

            # If dtype is str, check for empty input
            if dtype == str and not temp_input:
                temp_input = None
                raise ValueError

        except ValueError:
            # Custom error message if dtype is int and input is not a valid integer
            if dtype == int:
                print("Input harus berupa angka.")
            else:
                print("Tidak bisa input kosong.")
                
    return temp_input

def bayarRental(totalHarga) :
    #assign money to trigger while
    uang = 0
    while uang < totalHarga :
        #Get the money
        uang = read_validated_input(int, "Masukkan Jumlah Uang : ")
        if uang == totalHarga :
            print("Terima Kasih")
            break
        elif uang > totalHarga :
            print("Terima Kasih\nUang kembali anda : {kembalian}".format(kembalian = uang - totalHarga))
            break
        elif uang < totalHarga :
            print("Uangnya anda kurang sebesar {kurang}".format(kurang = totalHarga - uang))

def read_data():
    #Check if the list mobil is not empty
    if len(mobil) > 0 :
        print("Pilih Apa yang Ingin Ditampilkan : ")
        print("1. Mobil-Mobil yang Tersedia")
        print("2. Penyedia-Penyedia Mobil")
        input_read = 0
        while input_read < 1 or input_read > 2 :
            #Get What user want to be display
            input_read = read_validated_input(int, "Masukkan Angka Sesuai yang Ingin Ditampilkan : ")
            if input_read == 1 :
                menampilkanMobil()
            elif input_read == 2 :
                menampilkanPenyediaMobil()
            else :
                print("Masukkan Angka yang Tertera")
    else :
        print("Tidak ada mobil yang available \n")
        

def menampilkanMobil() :
    #Check if the list car is not empty
    if len(mobil) > 0:
        #Print all the car
        print("Daftar Mobil")
        print("Index \tNama \t\tMuat Orang \tPenyedia \tTransmisi \tHarga Mulai Dari")

        for item in range(len(mobil)):            
            car = mobil[item]
            min_harga = min(penyedia['harga'] for penyedia in car['penyedia'])
            print(str(item) + " \t" + str(mobil[item]['nama']) + "\t\t " + str(mobil[item]['ukuran']) + " \t\t" + str(len(mobil[item]['penyedia'])) + " \t\t" + str(mobil[item]['transmisi']) + " \t" + str({}).format(min_harga)) 
    
    else :
        print("Tidak ada mobil yang available \n")

def menampilkanPenyediaMobil() :
    #Check if the list car is not empty
    if len(mobil) > 0 :
        #Get all the car's provider name
        nama_penyedia = []
        for car in mobil :
            for penyedia in car['penyedia'] :
                if penyedia['nama'] not in nama_penyedia :
                    nama_penyedia.append(penyedia['nama'])
        #Display all the car's provider
        for penyedia in range(len(nama_penyedia)) :
            print(f"{penyedia}. {nama_penyedia[penyedia]}")
        
        input_penyedia = len(nama_penyedia)
        while input_penyedia >= len(nama_penyedia) or input_penyedia < 0 :
            #Get the car's provider that want to be display
            input_penyedia = read_validated_input(int, "Masukkan Index Penyedia yang Ingin Ditampilkan : ")
            if input_penyedia < len(nama_penyedia) and input_penyedia >= 0 :
                print("Nama Mobil\t Harga Mobil\t Plat Mobil")
                for car in mobil :
                    for penyedia in car['penyedia'] :
                        if nama_penyedia[input_penyedia] == penyedia['nama'] :
                            print(f"{car['nama']}\t\t {penyedia['harga']}\t\t ", ", ".join(penyedia['plat']))
            else :
                print("Masukkan Angka yang Tertera")
    else :
        print("Tidak ada mobil yang available \n")


def menampilkanMobilrental(rent) :
    #Check if the rent car is not empty
    if len(rent) > 0 :
        #Print all the car
        print("Daftar Mobil")
        print("Index \tNama\t\t Penyedia\t Transmisi \tPlat")
        for item in range(len(rent)) :
            print(str(item) + " \t" + str(rent[item]['nama']) + "\t\t " + str(rent[item]['penyedia']['nama']) + "\t " + str(rent[item]['transmisi']) + " \t" + str(rent[item]['penyedia']['plat']) )
    else :
        print("BELUM ADA MOBIL YANG DI PINJAM \n")

def menambahMobil():
    # List of existing car names
    mobilYgSudahAda = [exist['nama'] for exist in mobil]

    nama_mobil = read_validated_input(str, "Masukkan Nama Mobil: ")
    penyedia = read_validated_input(str, "Masukkan Nama Penyedia Mobil: ")

    # Loop until a valid plat is provided
    duplicate_found = True
    while duplicate_found == True:
        plat = read_validated_input(str, "Masukkan Plat Mobil yang Anda Miliki: ")
        duplicate_found = False

        for car in mobil:
            for provider in car['penyedia']:
                if plat in provider['plat']:
                    print(f"Plat '{plat}' sudah ada untuk penyedia '{provider['nama']}' di mobil '{car['nama']}'. Masukkan plat lain.")
                    duplicate_found = True
                    break
            if duplicate_found:
                break
        
    if nama_mobil in mobilYgSudahAda:
        # If the car already exists
        for car in mobil:
            if car['nama'] == nama_mobil:
                # Check if the provider already exists
                penyedia_found = False
                for provider in car['penyedia']:
                    if provider['nama'] == penyedia:
                        # Add plate to existing provider
                        provider['plat'].append(plat)
                        penyedia_found = True
                        break
                
                if not penyedia_found:
                    # Add a new provider
                    harga = read_validated_input(int, "Masukkan harga mobil per hari: ")
                    car['penyedia'].append({
                        'nama': penyedia,
                        'harga': harga,
                        'plat': [plat]
                    })

    else: 
        harga = read_validated_input(int, "Masukkan harga mobil per hari: ")
        ukuran = read_validated_input(int, "Masukkan Ukuran Muat Orang: ")
        transmisi = ''
        while transmisi != 'Automatic' and transmisi != 'Manual' :
            transmisi = read_validated_input(str, "Masukkan Transmisi Mobil (Automatic/Manual): ")
            if transmisi != 'Automatic' and transmisi != 'Manual' :
                print("Masukkan Automatic atau Manual")

        # Append new car data
        mobil.append({
            'nama': nama_mobil,
            'penyedia': [{
                'nama': penyedia,
                'harga': harga,
                'plat': [plat]
            }],
            'ukuran': ukuran,
            'transmisi': transmisi
        })
    print("\nMobil Anda Sudah Berhasil Ditambah \n")

def menghapusMobil() :
    #Check if list mobil is not empty
    if len(mobil) > 0 :
        menampilkanMobil()
        delete_mobil = False
        index = len(mobil) + 1
        while (index >= len(mobil) or index < 0):
            #Get the car that want to be deleted
            index = read_validated_input(int,"Masukkan index Mobil : ")
            if index < len(mobil) and index >= 0:
                print("Mobil yang dipilih : " + mobil[index]['nama'])
                print("Index \tPenyedia")
                for item in range(len(mobil[index]['penyedia'])) :
                    print(str(item) + " \t" + str(mobil[index]['penyedia'][item]['nama']))

                penyedia = len(mobil[index]['penyedia']) + 1
                while (penyedia >= len(mobil[index]['penyedia']) or penyedia < 0):
                    #Get the car's provider that want to be deleted
                    penyedia = read_validated_input(int,"Masukkan Index Penyedia Mobil : ")
                    if penyedia < len(mobil[index]['penyedia']) and penyedia >= 0 :
                        print("Penyedia yang dipilih : " + mobil[index]['penyedia'][penyedia]['nama'])
                        print("Index \tPlat")    
                        for num in range(len(mobil[index]['penyedia'][penyedia]['plat'])) :
                            print(f"{num} \t{mobil[index]['penyedia'][penyedia]['plat'][num]}")

                        plat = len(mobil[index]['penyedia'][penyedia]['plat']) + 1
                        while plat >= len(mobil[index]['penyedia'][penyedia]['plat']) or plat < 0 :
                            #Get What car based on plat that want to be deleted
                            plat = read_validated_input(int,"Masukkan Index Plat Mobil Yang Ingin Dihapus : ")
                            if plat < len(mobil[index]['penyedia'][penyedia]['plat']) or plat >= 0 :
                                print(f"Satu Mobil {mobil[index]['nama']} telah dihapus oleh penyedia {mobil[index]['penyedia'][item]['nama']}")    
                                delete_mobil = True
                    else :
                        print("Masukkan angka sesuai index")
            else :
                print("Masukkan angka sesuai index")
        #Delete the car from the list based on condition
        if delete_mobil :
            mobil[index]['penyedia'][penyedia]['plat'].pop(plat)
            #Delete the provider if there's no car 
            if len( mobil[index]['penyedia'][penyedia]['plat']) == 0 :
                mobil[index]['penyedia'].pop(penyedia)
            #Delete the car if there's no provider
            if len(mobil[index]['penyedia']) == 0 :
                mobil.pop(index)
    else :
        print("Tidak ada yang bisa dihapus \n")
           
def merentalMobil() :
    #Check if list mobil is not empty
    if len(mobil) > 0 :
        menampilkanMobil()
        rent_mobil = False
        pilihMobil = len(mobil) + 1
        while pilihMobil >= len(mobil) or pilihMobil < 0 :
            #Get the Car that want to be rented
            pilihMobil = read_validated_input(int,"Pilih Index Mobil Untuk Dirental: ")
            if pilihMobil < len(mobil) and pilihMobil >= 0 : 
                print("Mobil Pilihan : " + mobil[pilihMobil]['nama'])
                print("Index \tPenyedia \tHarga \tTersedia")
                for i in range(len(mobil[pilihMobil]['penyedia'])) :
                    print(f"{i} \t{mobil[pilihMobil]['penyedia'][i]['nama']} \t{str(mobil[pilihMobil]['penyedia'][i]['harga'])} \t{str(len(mobil[pilihMobil]['penyedia'][i]['plat']))} mobil")

                pilihPenyedia = len(mobil[pilihMobil]['penyedia']) + 1
                while pilihPenyedia >= len(mobil[pilihMobil]['penyedia']) or pilihPenyedia < 0 : 
                    #Get the Car's provider that want to be rented
                    pilihPenyedia = read_validated_input(int,"Pilih Index Penyedia Mobil : ")
                    if pilihPenyedia < len(mobil[pilihMobil]['penyedia']) and pilihPenyedia >= 0 :
                        hari = read_validated_input(int,"Masukkan Berapa Hari Ingin Merental Mobil : ")
                        totalHarga = mobil[pilihMobil]['penyedia'][pilihPenyedia]['harga'] * hari
                        
                        rand = random.randint(0,len(mobil[pilihMobil]['penyedia'][pilihPenyedia]['plat'])-1)
                        plat = mobil[pilihMobil]['penyedia'][pilihPenyedia]['plat'][rand]
                        
                        print("Mobil yg Dipilih \tPenyedia \tHarga \tHari Peminjaman \tPlat")
                        print(f"{mobil[pilihMobil]['nama']} \t\t{mobil[pilihMobil]['penyedia'][pilihPenyedia]['nama']} \t{str(mobil[pilihMobil]['penyedia'][pilihPenyedia]['harga'])} \t{hari} hari \t{str(plat)}") 
                        print(f"Total Harga : {totalHarga}")

                        bayarRental(totalHarga)
                        rent_mobil = True
                        #Add value to the list
                        mobilSedangDirental.append({
                            'nama' : mobil[pilihMobil]['nama'],
                            'penyedia' : {
                                'nama' : mobil[pilihMobil]['penyedia'][pilihPenyedia]['nama'],
                                'harga' : mobil[pilihMobil]['penyedia'][pilihPenyedia]['harga'],
                                'plat' : plat
                            },
                            'ukuran' : mobil[pilihMobil]['ukuran'],
                            'transmisi' : mobil[pilihMobil]['transmisi']
                        })
                    else :
                        print("Masukkan Angka Sesuai Index")
            else :
                print("Masukkan Angka Sesuai Index")
        if rent_mobil :
            mobil[pilihMobil]['penyedia'][pilihPenyedia]['plat'].pop(rand)
            
            if len( mobil[pilihMobil]['penyedia'][pilihPenyedia]['plat']) == 0 :
                mobil[pilihMobil]['penyedia'].pop(pilihPenyedia)
            
            if len( mobil[pilihMobil]['penyedia']) == 0 :
                mobil.pop(pilihMobil)
    else :
        print("Tidak ada mobil yang dapat dirental")


def updateMobil() :
    #Check if list mobil is not empty
    if len(mobil) > 0 :
        #Display the cars
        menampilkanMobil()
        index = len(mobil) + 1
        while (index >= len(mobil) or index < 0):
            #Get The Car the want to be update
            index = read_validated_input(int,"Masukkan index Mobil : ")
            if index < len(mobil) and index >= 0:
                print("Mobil yang dipilih : " + mobil[index]['nama'])
                print("Index \tPenyedia")
                for item in range(len(mobil[index]['penyedia'])) :
                    print(str(item) + " \t" + str(mobil[index]['penyedia'][item]['nama']))

                penyedia = len(mobil[index]['penyedia']) + 1
                while (penyedia >= len(mobil[index]['penyedia']) or penyedia < 0):
                    #Get the provider
                    penyedia = read_validated_input(int,"Masukkan Index Penyedia Mobil : ")
                    if penyedia < len(mobil[index]['penyedia']) and penyedia >= 0 :
                        print("Penyedia yang dipilih : " + mobil[index]['penyedia'][penyedia]['nama'])
                        input_update = 0
                        while input_update < 1 or input_update > 2 :
                            print("Informasi apa yang ingin diubah : ")
                            print("1. Harga Mobil")
                            input_update = read_validated_input(int, "Pilih yang ingin diubah : ")
                            if input_update == 1 :
                                print(f"Harga Mobil Anda Sekarang : {mobil[index]['penyedia'][penyedia]['harga']}")
                                input_update_harga = mobil[index]['penyedia'][penyedia]['harga']
                                while input_update_harga == mobil[index]['penyedia'][penyedia]['harga'] :
                                    input_update_harga = read_validated_input(int, "Masukkan Harga Baru : ")
                                    #If The input is same as the value
                                    if input_update_harga == mobil[index]['penyedia'][penyedia]['harga'] :
                                        print("Harga Mobil Anda Masih Sama")
                                    else :
                                        #Update a new price
                                        mobil[index]['penyedia'][penyedia]['harga'] = input_update_harga
                                        input_update_harga = 0
                                        print("Harga Mobil Anda Berhasil Diubah")
                            else :
                                print("Masukkan Angka Sesuai yg Tertera")
                    else :
                        print("Masukkan Angka Sesuai Index")
            else :
                print("Masukkan Angka Sesuai Index")
    else :
        print("Tidak ada mobil yang tersedia")

def mengembalikanMobil(mobilSedangDirental):
    menampilkanMobilrental(mobilSedangDirental)
    if len(mobilSedangDirental) > 0:
        pilih_mobil = len(mobilSedangDirental) + 1
        while pilih_mobil >= len(mobilSedangDirental) or pilih_mobil < 0:
            pilih_mobil = read_validated_input(int, "Pilih Index Mobil yang Sudah Selesai Digunakan: ")
            if 0 <= pilih_mobil < len(mobilSedangDirental):
                ada_mobil = False
                
                # Check if the car already exists in the mobil list
                for car in mobil:
                    if car['nama'] == mobilSedangDirental[pilih_mobil]['nama']:
                        ada_mobil = True
                        penyedia_found = False
                        
                        # Check if the penyedia exists for this car
                        for penyedia in car['penyedia']:
                            if penyedia['nama'] == mobilSedangDirental[pilih_mobil]['penyedia']['nama']:
                                penyedia['plat'].append(mobilSedangDirental[pilih_mobil]['penyedia']['plat'])
                                penyedia_found = True
                                break
                        
                        # If penyedia does not exist, add a new penyedia entry
                        if not penyedia_found:
                            car['penyedia'].append({
                                'nama': mobilSedangDirental[pilih_mobil]['penyedia']['nama'],
                                'harga': int(mobilSedangDirental[pilih_mobil]['penyedia']['harga']),
                                'plat': [mobilSedangDirental[pilih_mobil]['penyedia']['plat']]
                            })
                        break
                
                # If the car does not exist, add it as a new entry
                if not ada_mobil:
                    mobil.append({
                        'nama': mobilSedangDirental[pilih_mobil]['nama'],
                        'penyedia': [{
                            'nama': mobilSedangDirental[pilih_mobil]['penyedia']['nama'],
                            'harga': int(mobilSedangDirental[pilih_mobil]['penyedia']['harga']),
                            'plat': [mobilSedangDirental[pilih_mobil]['penyedia']['plat']]
                        }],
                        'ukuran': mobilSedangDirental[pilih_mobil]['ukuran'],
                        'transmisi': mobilSedangDirental[pilih_mobil]['transmisi']
                    })
                print("Mobil berhasil dikembalikan!")
            else:
                print("Masukkan Angka Sesuai Index")
        # Remove the returned car from the rental list
        del mobilSedangDirental[pilih_mobil]
    else:
        pass


InputUser = 0

while InputUser != 8 :
    print("Selamat datang di Rental Mobil")
    print("List Menu: ")
    print("1. Menampilkan Daftar Mobil")
    print("2. Menampilkan Daftar Mobil Yang Sedang Dirental")
    print("3. Menambah Mobil")
    print("4. Menghapus Mobil")
    print("5. Merental Mobil")
    print("6. Update Informasi Mobil")
    print("7. Mengembalikkan Mobil")
    print("8. Exit Program")

    InputUser = read_validated_input(int, "Masukkan Menu yang Diinginkan : ")

    if InputUser == 1 :
        read_data()
    elif InputUser == 2 :
        menampilkanMobilrental(mobilSedangDirental)
    elif InputUser == 3 :
        menambahMobil()
    elif InputUser == 4 :
        menghapusMobil()
    elif InputUser == 5 :
        merentalMobil() 
    elif InputUser == 6 :
        updateMobil()
    elif InputUser == 7 :
        mengembalikanMobil(mobilSedangDirental)
    elif InputUser < 1 or InputUser > 8:
        print("MASUKKAN ANGKA SESUAI YANG TERTERA \n")
