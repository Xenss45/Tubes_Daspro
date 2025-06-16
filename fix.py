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

# Kursi untuk setiap film dan jam (50 kursi, 0=kosong, 1=terisi)
# Film 1
film1_jam1 = [0] * 50
film1_jam2 = [0] * 50
film1_jam3 = [0] * 50

# Film 2
film2_jam1 = [0] * 50
film2_jam2 = [0] * 50
film2_jam3 = [0] * 50

# Film 3
film3_jam1 = [0] * 50
film3_jam2 = [0] * 50
film3_jam3 = [0] * 50

# Film 4
film4_jam1 = [0] * 50
film4_jam2 = [0] * 50
film4_jam3 = [0] * 50

# Data pemesanan (maksimal 100 pemesanan)
nama_pemesan = [""] * 100
film_pilihan = [""] * 100
jam_pilihan = [""] * 100
jumlah_tiket = [0] * 100
total_bayar = [0] * 100
jumlah_pesanan = 0

def tampilkan_film():
    print()
    print("=== DAFTAR FILM ===")
    print("1.", film1)
    print("2.", film2)
    print("3.", film3)
    print("4.", film4)

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
    for i in range(50):
        if kursi_data[i] == 0:
            kursi_kosong = kursi_kosong + 1
    
    return kursi_kosong

def tampilkan_kursi(pilihan_film, pilihan_jam):
    print()
    print("=== DENAH KURSI ===")
    print("0 = Kosong, 1 = Terisi")
    
    # Pilih data kursi yang sesuai
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
    
    # Tampilkan kursi
    for i in range(50):
        print("Kursi", i+1, ":", kursi_data[i])

def pesan_tiket():
    global jumlah_pesanan
    
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
    
    tampilkan_kursi(pilihan_film, pilihan_jam)
    kursi_dipilih = [0] * jumlah
    
    for i in range(jumlah):
        print()
        flag = False
        while not flag:
            tersedia = False
            print("Pilih kursi ke-" + str(i+1) + " (1-50):")
            nomor_kursi = int(input())
        
            if nomor_kursi < 1 or nomor_kursi > 50:
                print("Nomor kursi tidak valid!")
            
            if pilihan_film == 1 and pilihan_jam == 1:
                if film1_jam1[nomor_kursi-1] == 1:
                    print("Kursi sudah terisi!")
                    
                else:
                    tersedia = True
                    film1_jam1[nomor_kursi-1] = 1
            elif pilihan_film == 1 and pilihan_jam == 2:
                if film1_jam2[nomor_kursi-1] == 1:
                    print("Kursi sudah terisi!")
                    
                else:
                    tersedia = True
                    film1_jam2[nomor_kursi-1] = 1
            elif pilihan_film == 1 and pilihan_jam == 3:
                if film1_jam3[nomor_kursi-1] == 1:
                    print("Kursi sudah terisi!")
                    
                else:
                    tersedia = True
                    film1_jam3[nomor_kursi-1] = 1
            elif pilihan_film == 2 and pilihan_jam == 1:
                if film2_jam1[nomor_kursi-1] == 1:
                    print("Kursi sudah terisi!")
                    
                else:
                    tersedia = True
                    film2_jam1[nomor_kursi-1] = 1
            elif pilihan_film == 2 and pilihan_jam == 2:
                if film2_jam2[nomor_kursi-1] == 1:
                    print("Kursi sudah terisi!")
                    
                else:
                    tersedia = True
                    film2_jam2[nomor_kursi-1] = 1
            elif pilihan_film == 2 and pilihan_jam == 3:
                if film2_jam3[nomor_kursi-1] == 1:
                    print("Kursi sudah terisi!")
                    
                else:
                    tersedia = True
                    film2_jam3[nomor_kursi-1] = 1
            elif pilihan_film == 3 and pilihan_jam == 1:
                if film3_jam1[nomor_kursi-1] == 1:
                    print("Kursi sudah terisi!")
                    
                else:
                    tersedia = True
                    film3_jam1[nomor_kursi-1] = 1
            elif pilihan_film == 3 and pilihan_jam == 2:
                if film3_jam2[nomor_kursi-1] == 1:
                    print("Kursi sudah terisi!")
                else:
                    tersedia = True  
                    film3_jam2[nomor_kursi-1] = 1
            elif pilihan_film == 3 and pilihan_jam == 3:
                if film3_jam3[nomor_kursi-1] == 1:
                    print("Kursi sudah terisi!")
                
                else:
                    film3_jam3[nomor_kursi-1] = 1
                    tersedia = True
                    
            
            if tersedia == True :
                kursi_dipilih[i] = nomor_kursi
                flag = True
            
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
    
    
    jumlah_tiket[jumlah_pesanan] = jumlah
    total_bayar[jumlah_pesanan] = jumlah * harga
    
    jumlah_pesanan = jumlah_pesanan + 1
    print()
    print("=== TIKET BERHASIL DIPESAN ===")
    print("Nama:", nama)
    print("Total bayar: Rp", jumlah * harga)

def lihat_pemesanan():
    print()
    print("=== DAFTAR PEMESANAN ===")
    if jumlah_pesanan == 0:
        print("Belum ada pemesanan")
    else:
        for i in range(jumlah_pesanan):
            print(str(i+1) + ".", nama_pemesan[i], "-", film_pilihan[i], "(" + jam_pilihan[i] + ") -", jumlah_tiket[i], "tiket")

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