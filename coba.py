# Film dengan 3 jadwal waktu berbeda
film1 = [1, "Avengers: Endgame", 50, ["10:00", "14:00", "18:00"]]
film2 = [2, "Inception", 50, ["11:00", "15:00", "19:00"]]
film3 = [3, "Interstellar", 50, ["12:00", "16:00", "20:00"]]
film4 = [4, "The Batman", 50, ["13:00", "17:00", "21:00"]]

HARGA_TIKET = 30000
BATAS_DISKON = 5
DISKON = 10  

kursi_film1 = [[0] * 50, [0] * 50, [0] * 50]
kursi_film2 = [[0] * 50, [0] * 50, [0] * 50]
kursi_film3 = [[0] * 50, [0] * 50, [0] * 50]
kursi_film4 = [[0] * 50, [0] * 50, [0] * 50]

nama_pemesan = [""] * 100
film_dipesan = [""] * 100
jadwal_dipesan = [""] * 100
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

def get_film_data(film_id):
    """Mendapatkan data film berdasarkan ID"""
    if film_id == 1:
        return film1
    elif film_id == 2:
        return film2
    elif film_id == 3:
        return film3
    elif film_id == 4:
        return film4
    return None

def get_kursi_array(film_id):
    """Mendapatkan array kursi berdasarkan film ID"""
    if film_id == 1:
        return kursi_film1
    elif film_id == 2:
        return kursi_film2
    elif film_id == 3:
        return kursi_film3
    elif film_id == 4:
        return kursi_film4
    return None

def hitung_kursi_kosong(film_id, jadwal_index):
    """Menghitung jumlah kursi yang masih kosong untuk film dan jadwal tertentu"""
    kursi_array = get_kursi_array(film_id)
    if kursi_array is None:
        return 0
    
    jumlah_kosong = 0
    for kursi in kursi_array[jadwal_index]:
        if kursi == 0:
            jumlah_kosong += 1
    return jumlah_kosong

def tampilkan_film():
    """Menampilkan daftar film dengan jadwal"""
    print("\n--- Daftar Film ---")
    daftar_film = [film1, film2, film3, film4]
    for film in daftar_film:
        print(f"{film[0]}. {film[1]}")
        for i in range(len(film[3])):
            jadwal = film[3][i]
            kursi_kosong = hitung_kursi_kosong(film[0], i)
            print(f"   Jadwal {i+1}: {jadwal} ({kursi_kosong} kursi tersedia)")

def tampilkan_jadwal_film(film_id):
    """Menampilkan jadwal untuk film tertentu"""
    film_data = get_film_data(film_id)
    if film_data is None:
        return
    
    print(f"\nJadwal untuk {film_data[1]}:")
    for i in range(len(film_data[3])):
        jadwal = film_data[3][i]
        kursi_kosong = hitung_kursi_kosong(film_id, i)
        print(f"{i+1}. {jadwal} ({kursi_kosong} kursi tersedia)")

def tampilkan_kursi(film_id, jadwal_index):
    """Menampilkan layout kursi untuk film dan jadwal tertentu"""
    film_data = get_film_data(film_id)
    kursi_array = get_kursi_array(film_id)
    
    if film_data is None or kursi_array is None:
        return
    
    kursi = kursi_array[jadwal_index]
    nama_film = film_data[1]
    jadwal = film_data[3][jadwal_index]
    print()
    print(f"Kursi untuk {nama_film} - Jadwal {jadwal}:")
    print("Nomor kursi: ", end="")
    for i in range(len(kursi)):
        print(f"{i+1:2}", end=" ")  
    print()
    
    print("Status     : ", end="")
    for i in range(len(kursi)):
        if kursi[i] == 0:
            print("[ ]", end="")
        else:
            print("[X]", end="")
    print()
    print("Keterangan: [ ] = Kosong, [X] = Terisi")

def pesan_tiket():
    """Fungsi untuk memesan tiket"""
    global jumlah_pemesanan
    
    tampilkan_film()
    print()
    film_id = input_angka("Masukkan ID film yang ingin dipesan: ")
    
    if film_id < 1 or film_id > 4:
        print("❌ Film tidak ditemukan. Silakan coba lagi.")
        return
    
    
    tampilkan_jadwal_film(film_id)
    jadwal_pilihan = input_angka("Pilih jadwal (1-3): ") - 1
    
    if jadwal_pilihan < 0 or jadwal_pilihan > 2:
        print("❌ Jadwal tidak valid. Silakan coba lagi.")
        return
    
    nama = input("Masukkan nama Anda: ")
    
    kursi_tersedia = hitung_kursi_kosong(film_id, jadwal_pilihan)
    
    if kursi_tersedia == 0:
        print("❌ Maaf, tiket untuk jadwal ini sudah habis.")
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
    
    print(f"Total harga: Rp{harga:,}")
    
    tampilkan_kursi(film_id, jadwal_pilihan)
    
    # Pilih kursi - gunakan array dengan ukuran tetap
    kursi_terpilih = [0] * jumlah  # Array untuk menyimpan kursi yang dipilih
    kursi_array = get_kursi_array(film_id)
    max_kursi = len(kursi_array[jadwal_pilihan])
    
    for i in range(jumlah):
        while True:
            nomor_kursi = input_angka(f"Pilih kursi {i+1} (1-{max_kursi}): ")
            
            # Konversi ke index array (mulai dari 0)
            index_kursi = nomor_kursi - 1
            
            if index_kursi >= 0 and index_kursi < max_kursi and kursi_array[jadwal_pilihan][index_kursi] == 0:
                # Cek duplikasi manual
                sudah_dipilih = False
                for j in range(i):  # Cek kursi yang sudah dipilih sebelumnya
                    if kursi_terpilih[j] == index_kursi:
                        sudah_dipilih = True
                        break
                
                if not sudah_dipilih:
                    kursi_terpilih[i] = index_kursi
                    break
                else:
                    print("❌ Kursi sudah dipilih sebelumnya. Silakan pilih kursi lain.")
            else:
                print("❌ Kursi tidak valid atau sudah dipesan. Silakan coba lagi.")
    
    # Tandai kursi sebagai terisi
    for i in range(jumlah):
        kursi_array[jadwal_pilihan][kursi_terpilih[i]] = 1
    
    # Simpan data pemesanan
    film_data = get_film_data(film_id)
    nama_pemesan[jumlah_pemesanan] = nama
    film_dipesan[jumlah_pemesanan] = film_data[1]
    jadwal_dipesan[jumlah_pemesanan] = film_data[3][jadwal_pilihan]
    jumlah_tiket[jumlah_pemesanan] = jumlah
    total_harga[jumlah_pemesanan] = harga
    
    # Salin kursi terpilih ke array global
    kursi_dipilih[jumlah_pemesanan] = [0] * jumlah
    for i in range(jumlah):
        kursi_dipilih[jumlah_pemesanan][i] = kursi_terpilih[i]
    
    jumlah_pemesanan = jumlah_pemesanan + 1
    
    # Buat array untuk display kursi (mulai dari 1)
    kursi_display = [0] * jumlah
    for i in range(jumlah):
        kursi_display[i] = kursi_terpilih[i] + 1
    
    print(f"✅ Tiket berhasil dipesan!")
    print(f"   Film: {film_data[1]}")
    print(f"   Jadwal: {film_data[3][jadwal_pilihan]}")
    print(f"   Kursi: {kursi_display}")
    print(f"   Total harga: Rp{harga:,}")

def lihat_pemesanan():
    """Menampilkan daftar pemesanan"""
    print()
    print("--- Daftar Pemesanan ---")
    if jumlah_pemesanan == 0:
        print("Belum ada pemesanan.")
        return
    
    for i in range(jumlah_pemesanan):
        if nama_pemesan[i] != "":  # Pemesanan masih aktif
            # Konversi kursi ke nomor display (mulai dari 1)
            jumlah_kursi = jumlah_tiket[i]
            kursi_display = [0] * jumlah_kursi
            for j in range(jumlah_kursi):
                kursi_display[j] = kursi_dipilih[i][j] + 1
            
            print(f"{i+1}. {nama_pemesan[i]} - {film_dipesan[i]} ({jadwal_dipesan[i]})")
            print(f"    Tiket: {jumlah_tiket[i]} - Kursi: {kursi_display} - Total: Rp{total_harga[i]:,}")

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
    jadwal_yang_dibatalkan = jadwal_dipesan[nomor]
    kursi_yang_dibebaskan = kursi_dipilih[nomor]
    jumlah_kursi_dibebaskan = jumlah_tiket[nomor]
    
    # Cari film ID dan jadwal index
    film_id = None
    jadwal_index = None
    
    daftar_film = [film1, film2, film3, film4]
    for film in daftar_film:
        if film[1] == film_yang_dibatalkan:
            film_id = film[0]
            for i in range(len(film[3])):
                if film[3][i] == jadwal_yang_dibatalkan:
                    jadwal_index = i
                    break
            break
    
    if film_id is not None and jadwal_index is not None:
        kursi_array = get_kursi_array(film_id)
        for i in range(jumlah_kursi_dibebaskan):
            kursi_array[jadwal_index][kursi_yang_dibebaskan[i]] = 0
    
    print(f"✅ Pemesanan berhasil dibatalkan. Uang dikembalikan: Rp{total_harga[nomor]:,}")
    
    # Hapus data pemesanan
    nama_pemesan[nomor] = ""
    film_dipesan[nomor] = ""
    jadwal_dipesan[nomor] = ""
    jumlah_tiket[nomor] = 0
    total_harga[nomor] = 0
    kursi_dipilih[nomor] = []

def main():
    print()
    """Fungsi utama program"""
    while True:
        print("===== Aplikasi Tiket Bioskop =====")
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