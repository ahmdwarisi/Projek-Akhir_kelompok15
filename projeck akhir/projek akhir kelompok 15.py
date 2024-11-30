import random

pengiriman = {}

def tampilkan_pengiriman():
    if not pengiriman:
        print("Tidak ada data pengiriman yang tersimpan.")
    else:
        print("-"*50)
        print("Daftar Pengiriman:")
        print("-"*50)
        for resi, data in pengiriman.items():
            print(f"Resi: {resi}")
            print(f"  Nama Pengirim   : {data['pengirim']}")
            print(f"  Nama Penerima   : {data['penerima']}")
            print(f"  Alamat Tujuan   : {data['alamat']}")
            print(f"  Nama Barang     : {data['nama_barang']}")
            print(f"  Berat Barang    : {data['berat']}")
            print(f"  Harga pengiriman: {data['total_biaya']} ")
            print(f"  Diskon yang diperoleh : {data['diskon_yang_diperoleh']}")
            print(f"  Total Biaya Setelah diskon : {data['total_biaya_setelah_diskon']}")
            print(f"  Status Pengiriman: {data['status']}")
            print("-"*50)
    print()

def tambah_pengiriman():
    resi = f"WR{random.randint(1000, 9999)}"
    while resi in pengiriman:
        resi = f"WR{random.randint(1000, 9999)}"
    

    print(f"Nomor resi otomatis: {resi}")
    pengirim = input("Masukkan nama pengirim: ")
    penerima = input("Masukkan nama penerima: ")
    alamat = input("Masukkan alamat tujuan: ")
    nama_barang = input("Masukkan nama barang: ")

    while True:
        try:
            berat = float(input("Masukkan berat barang (kg): "))
            if berat <= 0:
                print("Berat barang harus lebih dari 0.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka desimal yang benar.")
    
    harga_per_kg = 10000
    total_biaya = berat * harga_per_kg

    diskon = 0
    if total_biaya > 100000:
        if total_biaya <= 250000:
            diskon = 0.05  #Diskon 5%
        elif total_biaya <= 500000:
            diskon = 0.10 #Diskon 10%
        else:
            diskon = 0.15  #Diskon 15%
    
    #Hitung total biaya setelah diskon
    total_biaya_setelah_diskon = total_biaya - (total_biaya * diskon)

    pengiriman[resi] = {
        "pengirim": pengirim,
        "penerima": penerima,
        "alamat": alamat,
        "nama_barang": nama_barang,
        "berat": berat,
        "harga_per_kg": harga_per_kg,
        "total_biaya": total_biaya,
        "diskon_yang_diperoleh":diskon,
        "total_biaya_setelah_diskon":total_biaya_setelah_diskon,
        "status": "Dalam proses pengiriman"
    }
    print(f"Pengiriman dengan resi {resi} berhasil ditambahkan.")
    print()

def perbarui_status():
    resi = input("Masukkan nomor resi yang ingin diperbarui: ")
    if resi in pengiriman:
        print("Status saat ini:", pengiriman[resi]['status'])
        status_baru = input("Masukkan status baru: ")
        pengiriman[resi]['status'] = status_baru
        print(f"Status pengiriman dengan resi {resi} berhasil diperbarui.")
    else:
        print(f"Pengiriman dengan resi {resi} tidak ditemukan.")
        print()

def hapus_pengiriman():
    resi = input("Masukkan Nomor Resi Barang yang akan di hapus: ")
    if resi in pengiriman:
        del pengiriman[resi]
        print(f"Data pengiriman dengan resi {resi} berhasil dihapus.")
    else:
        print(f"Tidak ditemukan data pengiriman dengan resi {resi}.")
    print()

while True:
    print("=== Menu ===")
    print("1. Tampilkan Pengiriman")
    print("2. Tambah Pengiriman")
    print("3. Perbarui Status Pengiriman")
    print("4. Hapus pengiriman")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    print()
    
    if pilihan == "1":
        tampilkan_pengiriman()
    elif pilihan == "2":
        tambah_pengiriman()
    elif pilihan == "3":
        perbarui_status()
    elif pilihan == "4":
        hapus_pengiriman()
    elif pilihan == "5":
        print("Program selesai. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
