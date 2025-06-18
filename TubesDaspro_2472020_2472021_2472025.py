# Nama file : TubesDaspro_2472020_2472021_2472025
# Penulis : Juan Alexander, Ferdinand Brian, Rafael Adiputra
# Tujuan program : Membuat agar user bisa memesan film berdasarkan film yang tersedia, jam tayang, memilih kursi, dan
# paket makanan yang tersedia. Menampilkan juga kursi mana yang tersedia dan sudah terisi
# -- Kamus Data - 
# pilihan : var. utk menyimpan pilihan user (int)
# film1, film2, film3, film4 : var. utk menyimpan nama film (str)
# jam1, jam2, jam3, jam4 : var. utk menyimpan jam tayang film (str)
# harga : var. utk harga tiket (int)
# angka : var. utk menyimpan nomor kursi (str)
# film1_jam1, film1_jam2, film1_jam3 : var. utk menyimpan data kursi film 1 pada jam ke 1, 2 dan 3 (int)
# film2_jam1, film2_jam2, film2_jam3 : var. utk menyimpan data kursi film 2 pada jam ke 1, 2 dan 3 (int)
# film3_jam1, film3_jam2, film3_jam3 : var. utk menyimpan data kursi film 3 pada jam ke 1, 2 dan 3 (int)
# film4_jam1, film4_jam2, film4_jam3 : var. utk menyimpan data kursi film 4 pada jam ke 1, 2 dan 3 (int)
# paket_makan : var. utk menyimpan data paket makanan (str, int)
# paket_pilihan : var. utk menyimpan nomor paket yang dipilih (int)
# nama_pemesanan : var. utk menyimpan nama user (str)
# film_pilihan : var. utk menyimpan film yang dipilih user (str)
# jam_pilihan : var. utk menyimpan jam tayang yang dipilih user (str)
# jumlah_tiket : var. utk menyimpan jumlah tiket yang dipesan user (int)
# total_bayar : var. utk menyimpan total harga yang harus dibayar user (int)
# jumlah_pesanan : var. utk menyimpan jumlah pemesanan yang sudah dilakukan (int)

# Data film sederhana
film1 = "Avengers: Endgame"
film2 = "Inception" 
film3 = "Interstellar"
film4 = "The Batman"

# Jam tayang untuk setiap film
jam1 = ["10:00", "14:00", "18:00"]
jam2 = ["11:00", "15:00", "19:00"] 
jam3 = ["12:00", "16:00", "20:00"]
jam4 = ["13:00", "17:00", "21:00"]

# Harga tiket
harga = 30000

# Angka untuk denah kursi
angka = ["1   2   3   4   5   6   7   8   9   10",
        "11  12  13  14  15  16  17  18  19  20",
        "21  22  23  24  25  26  27  28  29  30",
        "31  32  33  34  35  36  37  38  39  40",
        "41  42  43  44  45  46  47  48  49  50"]

# Kursi untuk setiap film dan jam (50 kursi, 0=kosong, 1=terisi)
# Film 1
film1_jam1 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]
film1_jam2 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]
film1_jam3 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]

# Film 2
film2_jam1 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]
film2_jam2 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]
film2_jam3 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]

# Film 3
film3_jam1 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]
film3_jam2 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]
film3_jam3 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]

# Film 4
film4_jam1 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]
film4_jam2 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]
film4_jam3 = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10]

# Paket paket
paket_makan = [
    {"nomor": "Paket 1","nama": "Popcorn kecil + Minuman", "harga": 15000},
    {"nomor": "Paket 2","nama": "Popcorn besar + Minuman", "harga": 20000},
    {"nomor": "Paket 3","nama": "Popcorn kecil & besar + Minuman", "harga": 30000}
]

paket_pilihan = [0] * 100  

# Data pemesanan (maksimal 100 pemesanan)
nama_pemesan = [""] * 100
film_pilihan = [""] * 100
jam_pilihan = [""] * 100
jumlah_tiket = [0] * 100
total_bayar = [0] * 100
jumlah_pesanan = 0

# Kamus lokal
# untuk menampilkan film yang tersedia
def tampilkan_film():
    print()
    print("=== DAFTAR FILM ===")
    print("1.", film1)
    print("2.", film2)
    print("3.", film3)
    print("4.", film4)

# Kamus lokal
# pilihan_film : parameter fungsi tampilkan_jam
# jam1, jam2, jam3, jam4 : var. utk menyimpan jam tayang film yang dipilih user (str)
def tampilkan_jam(pilihan_film):
    print()
    print("=== JAM TAYANG ===")
    if pilihan_film == 1:
        print("1.", jam1[0])
        print("2.", jam1[1])
        print("3.", jam1[2])
    elif pilihan_film == 2:
        print("1.", jam2[0])
        print("2.", jam2[1])
        print("3.", jam2[2])
    elif pilihan_film == 3:
        print("1.", jam3[0])
        print("2.", jam3[1])
        print("3.", jam3[2])
    elif pilihan_film == 4:
        print("1.", jam4[0])
        print("2.", jam4[1])
        print("3.", jam4[2])

# Kamus lokal
# pilihan_film, pilihan_jam : parameter fungsi hitung_kursi_kosong
# kursi_kosong : var. utk menyimpan jumlah kursi kosong (int)
# kursi_data : var. utk menyimpan data kursi yang dipilih user pada tiap jam tayang (int)
# film1_jam1, film1_jam2, film1_jam3 : var. utk menyimpan data kursi film 1 pada jam ke 1, 2 dan 3 (int)
# film2_jam1, film2_jam2, film2_jam3 : var. utk menyimpan data kursi film 2 pada jam ke 1, 2 dan 3 (int)
# film3_jam1, film3_jam2, film3_jam3 : var. utk menyimpan data kursi film 3 pada jam ke 1, 2 dan 3 (int)
# film4_jam1, film4_jam2, film4_jam3 : var. utk menyimpan data kursi film 4 pada jam ke 1, 2 dan 3 (int)
# baris, kolom : var. utk looping data kursi 
def hitung_kursi_kosong(pilihan_film, pilihan_jam):
    kursi_kosong = 0
    if pilihan_film == 1 and pilihan_jam == 1:
        kursi_data = film1_jam1
    elif pilihan_film == 1 and pilihan_jam == 2:
        kursi_data = film1_jam2
    elif pilihan_film == 1 and pilihan_jam == 3:
        kursi_data = film1_jam3
    elif pilihan_film == 2 and pilihan_jam == 1:
        kursi_data = film2_jam1
    elif pilihan_film == 2 and pilihan_jam == 2:
        kursi_data = film2_jam2
    elif pilihan_film == 2 and pilihan_jam == 3:
        kursi_data = film2_jam3
    elif pilihan_film == 3 and pilihan_jam == 1:
        kursi_data = film3_jam1
    elif pilihan_film == 3 and pilihan_jam == 2:
        kursi_data = film3_jam2
    elif pilihan_film == 3 and pilihan_jam == 3:
        kursi_data = film3_jam3
    elif pilihan_film == 4 and pilihan_jam == 1:
        kursi_data = film4_jam1
    elif pilihan_film == 4 and pilihan_jam == 2:
        kursi_data = film4_jam2
    elif pilihan_film == 4 and pilihan_jam == 3:
        kursi_data = film4_jam3
    
    # Hitung kursi kosong
    kursi_kosong = 0
    for baris in range(len(kursi_data)):
        for kolom in range(len(kursi_data[baris])):
            if kursi_data[baris][kolom] == 0:
                kursi_kosong += 1
    
    return kursi_kosong

# Kamus lokal
# pilihan_film, pilihan_jam : parameter fungsi tampilkan_kursi
# kursi_data : var. utk menyimpan data kursi yang dipilih user pada tiap jam tayang (int)
# film1_jam1, film1_jam2, film1_jam3 : var. utk menyimpan data kursi film 1 pada jam ke 1, 2 dan 3 (int)
# film2_jam1, film2_jam2, film2_jam3 : var. utk menyimpan data kursi film 2 pada jam ke 1, 2 dan 3 (int)
# film3_jam1, film3_jam2, film3_jam3 : var. utk menyimpan data kursi film 3 pada jam ke 1, 2 dan 3 (int)
# film4_jam1, film4_jam2, film4_jam3 : var. utk menyimpan data kursi film 4 pada jam ke 1, 2 dan 3 (int)
# baris, kolom : var. utk looping data kursi
def tampilkan_kursi(pilihan_film, pilihan_jam):
    print()
    print("=== DENAH KURSI ===")
    print("[ ] = Kosong, [x] = Terisi")

    kursi_data = []

    if pilihan_film == 1 and pilihan_jam == 1:
        kursi_data = film1_jam1
    elif pilihan_film == 1 and pilihan_jam == 2:
        kursi_data = film1_jam2
    elif pilihan_film == 1 and pilihan_jam == 3:
        kursi_data = film1_jam3
    elif pilihan_film == 2 and pilihan_jam == 1:
        kursi_data = film2_jam1
    elif pilihan_film == 2 and pilihan_jam == 2:
        kursi_data = film2_jam2
    elif pilihan_film == 2 and pilihan_jam == 3:
        kursi_data = film2_jam3
    elif pilihan_film == 3 and pilihan_jam == 1:
        kursi_data = film3_jam1
    elif pilihan_film == 3 and pilihan_jam == 2:
        kursi_data = film3_jam2
    elif pilihan_film == 3 and pilihan_jam == 3:
        kursi_data = film3_jam3
    elif pilihan_film == 4 and pilihan_jam == 1:
        kursi_data = film4_jam1
    elif pilihan_film == 4 and pilihan_jam == 2:
        kursi_data = film4_jam2
    elif pilihan_film == 4 and pilihan_jam == 3:
        kursi_data = film4_jam3

    baris = 0
    while baris < len(kursi_data):
        kolom = 0
        while kolom < len(kursi_data[baris]):
            if kursi_data[baris][kolom] == 0:
                print("[ ]", end=" ")
            else:
                print("[x]", end=" ")
            kolom += 1
        print()
        baris += 1

# Kamus lokal
# pilihan_film, pilihan_jam : parameter fungsi get_kursi_data
def get_kursi_data(pilihan_film, pilihan_jam):
    if pilihan_film == 1:
        return [film1_jam1, film1_jam2, film1_jam3][pilihan_jam - 1]
    elif pilihan_film == 2:
        return [film2_jam1, film2_jam2, film2_jam3][pilihan_jam - 1]
    elif pilihan_film == 3:
        return [film3_jam1, film3_jam2, film3_jam3][pilihan_jam - 1]
    elif pilihan_film == 4:
        return [film4_jam1, film4_jam2, film4_jam3][pilihan_jam - 1]

# Kamus lokal
# status : var. utk menyimpan status pemilihan film (bool)
# pilihan_film : var. input utk memilih film (int)
# status1 : var. utk menyimpan status pemilihan jam (bool)
# pilihan_jam : var. input utk memilih jam tayang (int)
# kursi_tersedia : var. utk memanggil fungsi hitung_kursi_kosong
# nama : var. input utk menyimpan nama user (str)
# status2 : var. utk menyimpan status pemilihan jumlah tiket (bool)
# jumlah : var. input utk menyimpan jumlah tiket yang dipesan (int)
# kursi_data : var. utk memanggil fungsi get_kursi_data
# kursi_dipilih : var. utk menyimpan kursi yang dipilih user (int)
# paket : var. input utk menyimpan pilihan paket makanan (int)
# paket_pilihan : var. utk menyimpan nomor paket yang dipilih user (int)
# harga_paket : var. utk menyimpan harga paket makanan (int)
# total : var. utk menyimpan total harga yang harus dibayar user (int)
# nama_pemesan, film_pilihan, jam_pilihan, jumlah_tiket, total_bayar : var. utk menyimpan data pemesanan
# tambah_paket : var. input utk menanyakan apakah user ingin menambah paket makanan atau tidak (str)
# paket_makan : var. utk menyimpan data paket makanan (str, int)
# nomor_kursi : var. input utk menyimpan nomor kursi yang dipilih user (int)
# baris, kolom : var. utk menyimpan posisi kursi yang dipilih user (int)
# jam_pilihan : var. utk menyimpan jam tayang yang dipilih user (str)
# film1, film2, film3, film4 : var. utk menyimpan nama film yang dipilih user (str)
# jam1, jam2, jam3, jam4 : var. utk menyimpan jam tayang yang dipilih user (str)
def pesan_tiket():
    global jumlah_pesanan
    global paket
    
    tampilkan_film()
    print()
    
    status = True
    while status == True:
        print("Pilih film (1-4):")
        pilihan_film = int(input())
        if pilihan_film < 1 or pilihan_film > 4:
            print("Film tidak ada!")
        else:
            status = False
        
    tampilkan_jam(pilihan_film)
    print()

    status1 = True
    while status1 == True:
        print("Pilih jam (1-3):")
        pilihan_jam = int(input())
        if pilihan_jam < 1 or pilihan_jam > 3:
            print("Jam tidak ada!")
        else:
            status1 = False
    
    kursi_tersedia = hitung_kursi_kosong(pilihan_film, pilihan_jam)
    print("Kursi tersedia:", kursi_tersedia)
    
    if kursi_tersedia == 0:
        print("Maaf, kursi sudah penuh!")
        return
    
    print()
    print("Masukkan nama:")
    nama = input()

    status2 = True
    while status2 == True:
        print("Jumlah tiket (maksimal", kursi_tersedia, "):")
        jumlah = int(input())
        if jumlah <= 0 or jumlah > kursi_tersedia:
            print("Jumlah tiket tidak valid!")
        else:
            status2 = False
    
    # Gunakan data kursi 2D
    kursi_data = get_kursi_data(pilihan_film, pilihan_jam)

    # Tampilkan denah kursi
    print()
    print("=== DENAH KURSI ===")
    print("[ ] = Kosong, [x] = Terisi")
    print()

    for i in range(len(kursi_data)):
        print(angka[i])  
        for kursi in kursi_data[i]:
            if kursi == 1:
                print("[x]" , end=" ")
            else :
                print("[ ]" , end=" ")
        print("")

   
    kursi_dipilih = [0] * jumlah  

    for i in range(jumlah):
        while True:
            print()
            nomor_kursi = int(input(f"Pilih kursi ke-{i+1} (1-50): "))
            if nomor_kursi < 1 or nomor_kursi > 50:
                print("Nomor kursi tidak valid!")
                continue

            baris = (nomor_kursi - 1) // 10
            kolom = (nomor_kursi - 1) % 10

            if kursi_data[baris][kolom] == 1:
                print("Kursi sudah terisi!")
            else:
                kursi_data[baris][kolom] = 1
                kursi_dipilih[i] = nomor_kursi  
                break
            
    nama_pemesan[jumlah_pesanan] = nama
    
    if pilihan_film == 1:
        film_pilihan[jumlah_pesanan] = film1
        if pilihan_jam == 1:
            jam_pilihan[jumlah_pesanan] = jam1[0]
        elif pilihan_jam == 2:
            jam_pilihan[jumlah_pesanan] = jam1[1]
        elif pilihan_jam == 3:
            jam_pilihan[jumlah_pesanan] = jam1[2]
    elif pilihan_film == 2:
        film_pilihan[jumlah_pesanan] = film2
        if pilihan_jam == 1:
            jam_pilihan[jumlah_pesanan] = jam2[0]
        elif pilihan_jam == 2:
            jam_pilihan[jumlah_pesanan] = jam2[1]
        elif pilihan_jam == 3:
            jam_pilihan[jumlah_pesanan] = jam2[2]
    elif pilihan_film == 3:
        film_pilihan[jumlah_pesanan] = film3
        if pilihan_jam == 1:
            jam_pilihan[jumlah_pesanan] = jam3[0]
        elif pilihan_jam == 2:
            jam_pilihan[jumlah_pesanan] = jam3[1]
        elif pilihan_jam == 3:
            jam_pilihan[jumlah_pesanan] = jam3[2]
    elif pilihan_film == 4:
        film_pilihan[jumlah_pesanan] = film4
        if pilihan_jam == 1:
            jam_pilihan[jumlah_pesanan] = jam4[0]
        elif pilihan_jam == 2:
            jam_pilihan[jumlah_pesanan] = jam4[1]
        elif pilihan_jam == 3:
            jam_pilihan[jumlah_pesanan] = jam4[2]


    jumlah_tiket[jumlah_pesanan] = jumlah 
    harga_tiket_total = jumlah * harga
    harga_paket = 0

    print()
    print("Apakah Anda ingin menambah makanan & minuman? (ya/tidak)")
    tambah_paket = input()

    if tambah_paket == "ya":
        print()
        print("=== PILIHAN PAKET paket ===")
        
        for i in range(len(paket_makan)):
            print(f"{i+1}. {paket_makan[i]['nomor']} : {paket_makan[i]['nama']}  Rp {paket_makan[i]['harga']}")
        
        while True:
            print("Pilih paket (1-3):")
            paket = int(input())
            if 1 <= paket <= len(paket_makan):
                harga_paket = paket_makan[paket - 1]["harga"]
                break
            else:
                print("Pilihan tidak valid!")
            harga_paket = paket_makan[paket - 1]["harga"]
        paket_pilihan[jumlah_pesanan] = paket  
    else:
        harga_paket = 0
        paket = 0
        paket_pilihan[jumlah_pesanan] = 0  


    total = harga_tiket_total + harga_paket
    total_bayar[jumlah_pesanan] = total
    jumlah_pesanan += 1

    print()
    print("=== TIKET BERHASIL DIPESAN ===")
    print("Nama               :", nama)
    print("Jumlah tiket       :", jumlah)
    if tambah_paket == "ya":
        print("Pilihan paket      :", paket_makan[paket - 1]['nama'])
    else :
        print("Pilihan paket      :", "(-)")
    print("Harga tiket        : Rp", harga_tiket_total)
    print("Harga paket        : Rp", harga_paket)
    print("Total yang dibayar : Rp", total)

# Kamus lokal 
# nama_pemesan, film_pilihan, jam_pilihan, jumlah_tiket, paket_pilihan : var. utk menyimpan data pemesanan
# paket_makan : var. utk menyimpan data paket makanan (str, int)
def lihat_pemesanan():
    print()
    print("=== DAFTAR PEMESANAN ===")
    if jumlah_pesanan == 0:
        print("Belum ada pemesanan")
    else:
        for i in range(jumlah_pesanan):
            print(str(i+1) + ".", nama_pemesan[i], "-", film_pilihan[i], "(" + jam_pilihan[i] + ") -", jumlah_tiket[i], "tiket",end="")
            if paket_pilihan[i] >= 1 and paket_pilihan[i] <= 3:
                print(" -", paket_makan[paket_pilihan[i] - 1]['nomor'],end="")
            print(" -",total_bayar[i])

# Program utama
def main():
    while True:
        print()
        print("===== Aplikasi Tiket Bioskop =====")
        print("1. Lihat film")
        print("2. Pesan tiket")
        print("3. Lihat pemesanan")
        print("4. Keluar")
        print("Pilih menu:")
        pilihan = int(input())
        
        if pilihan == 1:
            tampilkan_film()
        elif pilihan == 2:
            pesan_tiket()
        elif pilihan == 3:
            lihat_pemesanan()
        elif pilihan == 4:
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()