
# Daftar film dengan format: [ID, Nama Film, Jumlah Kursi]
daftar_film = [
    [1, "Avengers: Endgame", 20],
    [2, "Spider-Man: No Way Home", 25],
    [3, "The Batman", 15],
    [4, "Doctor Strange", 30],
    [5, "Top Gun: Maverick", 20]
]
# 💰 KONFIGURASI HARGA
HARGA_TIKET = 35000
MINIMAL_DISKON = 3  # Minimal tiket untuk dapat diskon
PERSENTASE_DISKON = 0.15  # Diskon 15%

# 🪑 SISTEM KURSI
# Membuat dictionary untuk menyimpan status kursi setiap film
kursi_film = {}
for film in daftar_film:
    film_id = film[0]
    jumlah_kursi = film[2]
    # Buat list kursi kosong untuk setiap film
    kursi_film[film_id] = ["KOSONG"] * jumlah_kursi

# 🎫 SISTEM TIKET
daftar_pemesanan = []  # List untuk menyimpan semua pemesanan
nomor_tiket = 1  # Counter untuk nomor tiket

def validasi_angka(teks_input):
    """
    Fungsi untuk memvalidasi input hanya berisi angka
    Input: string yang ingin divalidasi
    Output: True jika valid, False jika tidak
    """
    if not teks_input:  # Jika input kosong
        return False
    
    # Cek setiap karakter
    for karakter in teks_input:
        if karakter < '0' or karakter > '9':
            return False
    return True


def input_angka(pesan):
    """
    Fungsi untuk meminta input angka dengan validasi
    Input: pesan yang ditampilkan ke user
    Output: angka yang valid
    """
    while True:
        user_input = input(pesan)
        if validasi_angka(user_input):
            return int(user_input)
        print("❌ Harap masukkan angka yang valid!")


def tampilkan_garis():
    """Fungsi untuk menampilkan garis pemisah"""
    print("=" * 50)


def hitung_total_harga(jumlah_tiket):
    """
    Fungsi untuk menghitung total harga dengan diskon
    Input: jumlah tiket
    Output: total harga setelah diskon (jika ada)
    """
    total = jumlah_tiket * HARGA_TIKET
    
    # Cek apakah dapat diskon
    if jumlah_tiket >= MINIMAL_DISKON:
        diskon = total * PERSENTASE_DISKON
        total_setelah_diskon = total - diskon
        print(f"🎉 Selamat! Anda mendapat diskon {int(PERSENTASE_DISKON*100)}%")
        print(f"   Harga asli: Rp {total:,}")
        print(f"   Diskon: Rp {diskon:,}")
        print(f"   Total bayar: Rp {total_setelah_diskon:,}")
        return total_setelah_diskon
    
    return total

def tampilkan_menu_utama():
    """Fungsi untuk menampilkan menu utama"""
    tampilkan_garis()
    print("🎬 SISTEM BOOKING TIKET BIOSKOP 🎬")
    tampilkan_garis()
    print("1. 📋 Lihat Daftar Film")
    print("2. 🎫 Pesan Tiket")
    print("3. 📜 Lihat Daftar Pemesanan")
    print("4. ❌ Batalkan Pemesanan")
    print("5. 🪑 Lihat Status Kursi")
    print("6. 💰 Lihat Laporan Pendapatan")
    print("7. 🚪 Keluar")
    tampilkan_garis()

def tampilkan_daftar_film():
    """Fungsi untuk menampilkan semua film yang tersedia"""
    print("\n📋 DAFTAR FILM YANG TERSEDIA:")
    print("-" * 40)
    
    for film in daftar_film:
        film_id = film[0]
        nama_film = film[1]
        total_kursi = film[2]
        
        # Hitung kursi yang masih kosong
        kursi_kosong = kursi_film[film_id].count("KOSONG")
        kursi_terisi = total_kursi - kursi_kosong
        
        print(f"{film_id}. {nama_film}")
        print(f"   💺 Kursi tersedia: {kursi_kosong}/{total_kursi}")
        print(f"   💰 Harga: Rp {HARGA_TIKET:,}")
        print()

def tampilkan_status_kursi(film_id):
    """
    Fungsi untuk menampilkan status kursi suatu film
    Input: ID film
    """
    # Cari nama film berdasarkan ID
    nama_film = ""
    for film in daftar_film:
        if film[0] == film_id:
            nama_film = film[1]
            break
    
    print(f"\n🪑 STATUS KURSI - {nama_film}")
    print("-" * 40)
    print("Keterangan: [K] = Kosong, [X] = Terisi")
    print()
    # Tampilkan nomor kursi
    print("Nomor kursi:")
    for i in range(len(kursi_film[film_id])):
        print(f"{i+1:2d}", end=" ")
    print()
    # Tampilkan status kursi
    print("Status     :")
    for status in kursi_film[film_id]:
        if status == "KOSONG":
            print("[K]", end=" ")
        else:
            print("[X]", end=" ")
    print()

def tampilkan_semua_pemesanan():
    """Fungsi untuk menampilkan semua pemesanan"""
    print("\n📜 DAFTAR SEMUA PEMESANAN:")
    print("-" * 60)
    
    if not daftar_pemesanan:
        print("Belum ada pemesanan.")
        return
    
    for i, pemesanan in enumerate(daftar_pemesanan):
        if pemesanan:  # Jika pemesanan tidak dibatalkan
            print(f"Nomor Tiket: {i+1}")
            print(f"Nama: {pemesanan['nama']}")
            print(f"Film: {pemesanan['film']}")
            print(f"Jumlah Tiket: {pemesanan['jumlah']}")
            print(f"Kursi: {pemesanan['kursi']}")
            print(f"Total Bayar: Rp {pemesanan['total']:,}")
            print("-" * 30)

def pesan_tiket():
    """Fungsi untuk memesan tiket"""
    global nomor_tiket
    print("\n🎫 PEMESANAN TIKET")
    tampilkan_daftar_film()
    # Pilih film
    film_id = input_angka("Pilih ID film (1-5): ")
    # Validasi film ID
    if film_id < 1 or film_id > len(daftar_film):
        print("❌ Film tidak ditemukan!")
        return
    # Ambil data film
    nama_film = ""
    for film in daftar_film:
        if film[0] == film_id:
            nama_film = film[1]
            break
    # Cek kursi tersedia
    kursi_tersedia = kursi_film[film_id].count("KOSONG")
    if kursi_tersedia == 0:
        print("❌ Maaf, kursi sudah penuh!")
        return
    print(f"\n✅ Film dipilih: {nama_film}")
    print(f"💺 Kursi tersedia: {kursi_tersedia}")
    # Input nama pemesan
    nama_pemesan = input("Masukkan nama pemesan: ").strip()
    if not nama_pemesan:
        print("❌ Nama tidak boleh kosong!")
        return
    # Input jumlah tiket
    jumlah_tiket = input_angka("Jumlah tiket yang ingin dipesan: ")
    if jumlah_tiket <= 0 or jumlah_tiket > kursi_tersedia:
        print(f"❌ Jumlah tiket tidak valid! (Maksimal: {kursi_tersedia})")
        return
    # Hitung total harga
    total_harga = hitung_total_harga(jumlah_tiket)
    # Tampilkan kursi dan pilih kursi
    tampilkan_status_kursi(film_id)
    kursi_dipilih = []
    for i in range(jumlah_tiket):
        while True:
            nomor_kursi = input_angka(f"Pilih kursi ke-{i+1} (1-{len(kursi_film[film_id])}): ")
            
            # Validasi nomor kursi
            if nomor_kursi < 1 or nomor_kursi > len(kursi_film[film_id]):
                print("❌ Nomor kursi tidak valid!")
                continue
            
            # Cek apakah kursi masih kosong
            if kursi_film[film_id][nomor_kursi-1] != "KOSONG":
                print("❌ Kursi sudah terisi! Pilih kursi lain.")
                continue
            
            # Cek apakah kursi sudah dipilih sebelumnya
            if nomor_kursi in kursi_dipilih:
                print("❌ Kursi sudah dipilih! Pilih kursi lain.")
                continue
            
            kursi_dipilih.append(nomor_kursi)
            break
    # Konfirmasi pemesanan
    print(f"\n📋 KONFIRMASI PEMESANAN:")
    print(f"Nama: {nama_pemesan}")
    print(f"Film: {nama_film}")
    print(f"Jumlah Tiket: {jumlah_tiket}")
    print(f"Kursi: {kursi_dipilih}")
    print(f"Total Bayar: Rp {total_harga:,}")
    
    konfirmasi = input("\nKonfirmasi pemesanan? (y/n): ").lower()
    
    if konfirmasi == 'y' or konfirmasi == 'yes':
        # Tandai kursi sebagai terisi
        for kursi in kursi_dipilih:
            kursi_film[film_id][kursi-1] = "TERISI"    
        # Simpan pemesanan
        pemesanan_baru = {
            'nama': nama_pemesan,
            'film': nama_film,
            'jumlah': jumlah_tiket,
            'kursi': kursi_dipilih,
            'total': total_harga,
            'film_id': film_id
        }  
        daftar_pemesanan.append(pemesanan_baru)     
        print(f"\n✅ PEMESANAN BERHASIL!")
        print(f"Nomor Tiket Anda: {len(daftar_pemesanan)}")
        print("Simpan nomor tiket untuk referensi.")
        
    else:
        print("❌ Pemesanan dibatalkan.")

def batalkan_pemesanan():
    """Fungsi untuk membatalkan pemesanan"""
    if not daftar_pemesanan:
        print("❌ Belum ada pemesanan yang bisa dibatalkan.")
        return
    
    print("\n❌ PEMBATALAN PEMESANAN")
    tampilkan_semua_pemesanan()
    
    nomor_tiket_batal = input_angka("Masukkan nomor tiket yang ingin dibatalkan: ")
    
    if nomor_tiket_batal < 1 or nomor_tiket_batal > len(daftar_pemesanan):
        print("❌ Nomor tiket tidak valid!")
        return
    
    # Ambil data pemesanan (index dimulai dari 0)
    pemesanan = daftar_pemesanan[nomor_tiket_batal - 1]
    
    if not pemesanan:
        print("❌ Tiket sudah dibatalkan sebelumnya!")
        return
    
    # Tampilkan detail pemesanan
    print(f"\n📋 DETAIL PEMESANAN:")
    print(f"Nama: {pemesanan['nama']}")
    print(f"Film: {pemesanan['film']}")
    print(f"Kursi: {pemesanan['kursi']}")
    print(f"Total: Rp {pemesanan['total']:,}")
    
    konfirmasi = input("\nYakin ingin membatalkan? (y/n): ").lower()
    
    if konfirmasi == 'y' or konfirmasi == 'yes':
        # Kembalikan kursi menjadi kosong
        film_id = pemesanan['film_id']
        for kursi in pemesanan['kursi']:
            kursi_film[film_id][kursi-1] = "KOSONG"
        
        # Hapus pemesanan
        daftar_pemesanan[nomor_tiket_batal - 1] = None
        
        print(f"✅ Pemesanan berhasil dibatalkan!")
        print(f"💰 Uang dikembalikan: Rp {pemesanan['total']:,}")
    else:
        print("❌ Pembatalan dibatalkan.")

def lihat_status_kursi():
    """Fungsi untuk melihat status kursi semua film"""
    print("\n🪑 STATUS KURSI SEMUA FILM")
    
    for film in daftar_film:
        film_id = film[0]
        tampilkan_status_kursi(film_id)
        print()

def lihat_laporan():
    """Fungsi untuk melihat laporan pendapatan"""
    print("\n💰 LAPORAN PENDAPATAN")
    print("-" * 40)
    
    if not daftar_pemesanan:
        print("Belum ada transaksi.")
        return
    
    total_pendapatan = 0
    jumlah_tiket_terjual = 0
    
    for pemesanan in daftar_pemesanan:
        if pemesanan:  # Jika tidak dibatalkan
            total_pendapatan += pemesanan['total']
            jumlah_tiket_terjual += pemesanan['jumlah']
    
    print(f"Total Tiket Terjual: {jumlah_tiket_terjual}")
    print(f"Total Pendapatan: Rp {total_pendapatan:,}")
    
    # Statistik per film
    print("\n📊 STATISTIK PER FILM:")
    for film in daftar_film:
        film_id = film[0]
        nama_film = film[1]
        total_kursi = film[2]
        kursi_terisi = kursi_film[film_id].count("TERISI")
        persentase = (kursi_terisi / total_kursi) * 100
        
        print(f"{nama_film}: {kursi_terisi}/{total_kursi} ({persentase:.1f}%)")

def main():
    """Fungsi utama program"""
    print("Selamat datang di Sistem Booking Tiket Bioskop!")
    print("Program ini dibuat untuk membantu Anda belajar Python.")
    while True:
        tampilkan_menu_utama()
        pilihan = input("Pilih menu (1-7): ")
        if pilihan == "1":
            tampilkan_daftar_film()   
        elif pilihan == "2":
            pesan_tiket()    
        elif pilihan == "3":
            tampilkan_semua_pemesanan()  
        elif pilihan == "4":
            batalkan_pemesanan()  
        elif pilihan == "5":
            lihat_status_kursi()    
        elif pilihan == "6":
            lihat_laporan()    
        elif pilihan == "7":
            print("\n🎬 Terima kasih telah menggunakan sistem booking!")
            print("Sampai jumpa! 👋")
            break    
        else:
            print("❌ Pilihan tidak valid! Silakan pilih 1-7.")
        input("\nTekan Enter untuk kembali ke menu...")


# ====================================
# JALANKAN PROGRAM
# ====================================

if __name__ == "__main__":
    main()