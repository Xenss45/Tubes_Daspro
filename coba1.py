# Data film: [id, nama_film, jumlah_kursi]
film1 = [1, "Avengers: Endgame", 50]
film2 = [2, "Inception", 40]
film3 = [3, "Interstellar", 30]
film4 = [4, "The Batman", 25]

HARGA_TIKET = 30000
BATAS_DISKON = 5
DISKON = 10  # dalam persen

# Kursi untuk setiap film (0 = kosong, 1 = terisi)
kursi_film1 = [0] * film1[2]  # 50 kursi
kursi_film2 = [0] * film2[2]  # 40 kursi  
kursi_film3 = [0] * film3[2]  # 30 kursi
kursi_film4 = [0] * film4[2]  # 25 kursi

# Data pemesanan
nama_pemesan = [""] * 100
film_dipesan = [""] * 100
jumlah_tiket = [0] * 100
total_harga = [0] * 100
kursi_dipilih = [[] for i in range(100)]
jumlah_pemesanan = 0

def cek_angka(teks):
    """Mengecek apakah input adalah angka"""
    if len(teks) == 0:
        return False
    for karakter in teks:
        if karakter < '0' or karakter > '9':
            return False
    return True

def input_angka(pesan):
    """Meminta input angka dari user"""
    while True:
        nilai = input(pesan)
        if cek_angka(nilai):
            return int(nilai)
        print("❌ Input harus berupa angka. Silakan coba lagi.")

def hitung_kursi_kosong(film_id):
    """Menghitung jumlah kursi yang masih kosong"""
    if film_id == 1:
        return kursi_film1.count(0)
    elif film_id == 2:
        return kursi_film2.count(0)
    elif film_id == 3:
        return kursi_film3.count(0)
    elif film_id == 4:
        return kursi_film4.count(0)
    return 0

def tampilkan_film():
    """Menampilkan daftar film"""
    print("\n--- Daftar Film ---")
    print(f"{film1[0]}. {film1[1]} ({hitung_kursi_kosong(1)} kursi tersedia)")
    print(f"{film2[0]}. {film2[1]} ({hitung_kursi_kosong(2)} kursi tersedia)")
    print(f"{film3[0]}. {film3[1]} ({hitung_kursi_kosong(3)} kursi tersedia)")
    print(f"{film4[0]}. {film4[1]} ({hitung_kursi_kosong(4)} kursi tersedia)")

def tampilkan_kursi(film_id):
    """Menampilkan layout kursi"""
    if film_id == 1:
        kursi = kursi_film1
        nama_film = film1[1]
    elif film_id == 2:
        kursi = kursi_film2
        nama_film = film2[1]
    elif film_id == 3:
        kursi = kursi_film3
        nama_film = film3[1]
    elif film_id == 4:
        kursi = kursi_film4
        nama_film = film4[1]
    else:
        return
    
    print(f"\nKursi untuk {nama_film}:")
    print("Nomor kursi: ", end="")
    for i in range(len(kursi)):
        print(f"{i:2}", end=" ")
    print()
    
    print("Status     : ", end="")
    for i in range(len(kursi)):
        if kursi[i] == 0:
            print("[ ]", end="")
        else:
            print("[X]", end="")
    print()

def pesan_tiket():
    """Fungsi untuk memesan tiket"""
    global jumlah_pemesanan
    
    tampilkan_film()
    
    film_id = input_angka("\nMasukkan ID film yang ingin dipesan: ")
    
    if film_id < 1 or film_id > 4:
        print("❌ Film tidak ditemukan. Silakan coba lagi.")
        return
    
    nama = input("Masukkan nama Anda: ")
    
    kursi_tersedia = hitung_kursi_kosong(film_id)
    
    if kursi_tersedia == 0:
        print("❌ Maaf, tiket untuk film ini sudah habis.")
        return
    
    jumlah = input_angka("Jumlah tiket: ")
    
    if jumlah <= 0 or jumlah > kursi_tersedia:
        print("❌ Jumlah tiket tidak valid. Silakan coba lagi.")
        return
    
    # Hitung harga
    harga = jumlah * HARGA_TIKET
    if jumlah >= BATAS_DISKON:
        harga = harga - (harga * DISKON // 100)
        print(f"🎉 Anda mendapatkan diskon {DISKON}%!")
    
    print(f"Total harga: Rp{harga}")
    
    tampilkan_kursi(film_id)
    
    # Pilih kursi
    kursi_terpilih = []
    for i in range(jumlah):
        while True:
            if film_id == 1:
                max_kursi = len(kursi_film1) - 1
                kursi_array = kursi_film1
            elif film_id == 2:
                max_kursi = len(kursi_film2) - 1
                kursi_array = kursi_film2
            elif film_id == 3:
                max_kursi = len(kursi_film3) - 1
                kursi_array = kursi_film3
            elif film_id == 4:
                max_kursi = len(kursi_film4) - 1
                kursi_array = kursi_film4
            
            nomor_kursi = input_angka(f"Pilih kursi {i+1} (0-{max_kursi}): ")
            
            if nomor_kursi >= 0 and nomor_kursi <= max_kursi and kursi_array[nomor_kursi] == 0:
                kursi_terpilih.append(nomor_kursi)
                break
            else:
                print("❌ Kursi tidak valid atau sudah dipesan. Silakan coba lagi.")
    
    # Tandai kursi sebagai terisi
    for kursi in kursi_terpilih:
        if film_id == 1:
            kursi_film1[kursi] = 1
        elif film_id == 2:
            kursi_film2[kursi] = 1
        elif film_id == 3:
            kursi_film3[kursi] = 1
        elif film_id == 4:
            kursi_film4[kursi] = 1
    
    # Simpan data pemesanan
    nama_pemesan[jumlah_pemesanan] = nama
    if film_id == 1:
        film_dipesan[jumlah_pemesanan] = film1[1]
    elif film_id == 2:
        film_dipesan[jumlah_pemesanan] = film2[1]
    elif film_id == 3:
        film_dipesan[jumlah_pemesanan] = film3[1]
    elif film_id == 4:
        film_dipesan[jumlah_pemesanan] = film4[1]
    
    jumlah_tiket[jumlah_pemesanan] = jumlah
    total_harga[jumlah_pemesanan] = harga
    kursi_dipilih[jumlah_pemesanan] = kursi_terpilih.copy()
    
    jumlah_pemesanan = jumlah_pemesanan + 1
    
    print(f"✅ Tiket berhasil dipesan! Total harga: Rp{harga}")

def lihat_pemesanan():
    """Menampilkan daftar pemesanan"""
    print("\n--- Daftar Pemesanan ---")
    if jumlah_pemesanan == 0:
        print("Belum ada pemesanan.")
        return
    
    for i in range(jumlah_pemesanan):
        if nama_pemesan[i] != "":  # Pemesanan masih aktif
            print(f"{i+1}. {nama_pemesan[i]} memesan {jumlah_tiket[i]} tiket untuk '{film_dipesan[i]}' - Total: Rp{total_harga[i]} - Kursi: {kursi_dipilih[i]}")

def batalkan_pemesanan():
    """Membatalkan pemesanan"""
    lihat_pemesanan()
    if jumlah_pemesanan == 0:
        return
    
    nomor = input_angka("Masukkan nomor pesanan yang ingin dibatalkan: ") - 1
    
    if nomor < 0 or nomor >= jumlah_pemesanan or nama_pemesan[nomor] == "":
        print("❌ Nomor pesanan tidak valid. Silakan coba lagi.")
        return
    
    # Bebaskan kursi
    film_yang_dibatalkan = film_dipesan[nomor]
    kursi_yang_dibebaskan = kursi_dipilih[nomor]
    
    for kursi in kursi_yang_dibebaskan:
        if film_yang_dibatalkan == film1[1]:
            kursi_film1[kursi] = 0
        elif film_yang_dibatalkan == film2[1]:
            kursi_film2[kursi] = 0
        elif film_yang_dibatalkan == film3[1]:
            kursi_film3[kursi] = 0
        elif film_yang_dibatalkan == film4[1]:
            kursi_film4[kursi] = 0
    
    print(f"✅ Pemesanan berhasil dibatalkan. Uang dikembalikan: Rp{total_harga[nomor]}")
    
    # Hapus data pemesanan
    nama_pemesan[nomor] = ""
    film_dipesan[nomor] = ""
    jumlah_tiket[nomor] = 0
    total_harga[nomor] = 0
    kursi_dipilih[nomor] = []

def main():
    """Fungsi utama program"""
    while True:
        print("\n===== Aplikasi Tiket Bioskop =====")
        print("1. Lihat daftar film")
        print("2. Pesan tiket")
        print("3. Lihat daftar pemesanan")
        print("4. Batalkan pemesanan")
        print("5. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tampilkan_film()
        elif pilihan == "2":
            pesan_tiket()
        elif pilihan == "3":
            lihat_pemesanan()
        elif pilihan == "4":
            batalkan_pemesanan()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()