# Data film
film_list = [
    {"judul": "Spiderman: No Way Home", "jam":["14:00","15:00", "18:00", "21:00"], "harga": 35000},
    {"judul": "Oppenheimer", "jam":["14:00","15:00", "18:00", "21:00"], "harga": 35000},
    {"judul": "Kungfu Panda 4", "jam":["14:00","15:00", "18:00", "21:00"], "harga": 35000}
]

# Data makanan/minuman
fnb_list = [
    {"nama": "Popcorn", "harga": 40000},
    {"nama": "Coca-Cola", "harga": 25000}
]

# Data booking dan pesanan user
booking = {
    "film": "",
    "jam": "",
    "jumlah_tiket": 0,
    "kursi": [],
    "total_tiket": 0
}
pesanan_fnb = []
total_fnb = 0
total_bayar = 0
sudah_bayar = False

# Kursi tersedia
kursi_tersedia = ["A1", "A2", "A3", "A4", "A5", "A6",
"B1", "B2", "B3", "B4", "B5", "B6",
"C1", "C2", "C3", "C4", "C5", "C6",
"D1", "D2", "D3", "D4", "D5", "D6",]

def tampil_menu():
    print("=== SELAMAT DATANG DI BIOSKOP XXI ===")
    print("1. Lihat Daftar Film")
    print("2. Booking Tiket")
    print("3. Pesan Makanan/Minuman")
    print("4. Pembayaran")
    print("5. Cetak Resi Tiket")
    print("6. Keluar")
    pilih = input("Pilih menu: ")
    return pilih

def lihat_daftar_film():
    print()
    print("=== DAFTAR FILM YANG TERSEDIA ===")
    idx = 1
    for f in film_list:
        print(str(idx) + ". " + f["judul"] + " | " + str(f["jam"]) + " | Rp" + str(f["harga"]))
        idx += 1
    input("Tekan ENTER untuk kembali ke menu utama...")
    print()


def booking_tiket():
    global booking, kursi_tersedia, total_bayar, sudah_bayar
    print()
    print("=== BOOKING TIKET ===")
    idx = 1
    for f in film_list:
        print(str(idx) + ". " + f["judul"])
        idx = idx + 1
    pilih = input("Pilih film: ")
    film_idx = int(pilih) - 1
    film = film_list[film_idx]

    # Tampilkan pilihan jam tayang
    print("Pilih jam tayang:")
    idx_jam = 1
    for jam in film["jam"]:
        print(str(idx_jam) + ". " + jam)
        idx_jam = idx_jam + 1
    pilih_jam = input("Pilih jam tayang: ")
    jam_idx = int(pilih_jam) - 1

    booking["film"] = film["judul"]
    booking["jam"] = film["jam"][jam_idx]
    harga = film["harga"]
    jumlah = int(input("Pilih jumlah tiket: "))
    booking["jumlah_tiket"] = jumlah

    # Tampilkan kursi (dengan 'X' jika sudah dibooking)
    kursi_pilihan = []
    print("Kursi setelah dibooking:")
    for row in ["A", "B", "C", "D"]:
        baris = ""
        for num in range(1, 7):
            kode = row + str(num)
            if kode in kursi_pilihan:  # Jika kursi sudah dipilih, tampilkan 'X'
                baris += " X "
            else:
                baris += kode  # Jika belum dipilih, tampilkan kode kursi
            if num != 6:
                baris += " | "
        print(baris)

    # Input kursi satu per satu
    print("Masukkan " + str(jumlah) + " kursi satu per satu:")
    for i in range(jumlah):
        kursi = input("Kursi ke-" + str(i + 1) + ": ")
        kursi_pilihan = kursi_pilihan + [kursi]

    # Hapus kursi yang sudah dipilih dari kursi_tersedia
    kursi_baru = []
    for k in kursi_tersedia:
        ada = False
        for kp in kursi_pilihan:
            if k == kp:
                ada = True
        if not ada:
            kursi_baru = kursi_baru + [k]
    kursi_tersedia = kursi_baru

    booking["kursi"] = kursi_pilihan
    booking["total_tiket"] = harga * jumlah
    total_bayar = booking["total_tiket"] + total_fnb
    sudah_bayar = False
    print("Status: Tiket berhasil dibooking!")
    input("Tekan ENTER untuk kembali ke menu utama...")
    print()

def pesan_fnb():
    global pesanan_fnb, total_fnb, total_bayar, sudah_bayar
    print()
    print("=== PESAN MAKANAN & MINUMAN ===")
    ulang = "ya"
    while ulang == "ya":
        idx = 1
        for item in fnb_list:
            print(str(idx) + ". " + item["nama"] + " (Rp " + str(item["harga"])+')')
            idx = idx + 1

        pilih = input("Pilih item: ")
        idx_item = int(pilih) - 1
        item = fnb_list[idx_item]
        jumlah = int(input("Jumlah: "))
        ada = False
        for p in pesanan_fnb:
            if p["nama"] == item["nama"]:
                p["jumlah"] = p["jumlah"] + jumlah
                ada = True
        if not ada:
            pesanan_fnb = pesanan_fnb + [{"nama": item["nama"], "jumlah": jumlah, "harga": item["harga"]}]

        total_fnb = total_fnb + (item["harga"] * jumlah)
        total_bayar = booking["total_tiket"] + total_fnb
        print(str(jumlah) + " " + item["nama"] + " berhasil ditambahkan")
        sudah_bayar = False
        print()
        
        ulang = input("Apakah anda ingin memesan lagi? (ya/tidak): ")
        while ulang != "ya" and ulang != "tidak":
            print('Silahkan pilih ya/tidak')
            ulang = input("Apakah anda ingin memesan lagi? (ya/tidak): ")
    input("Tekan ENTER untuk kembali ke menu utama...")
    print()

def pembayaran():
    global total_bayar, sudah_bayar
    print()
    print("=== PEMBAYARAN ===")
    print("Total Tiket        : Rp " + str(booking["total_tiket"]))
    print("Total Makanan/Minum: Rp " + str(total_fnb))
    print('==========')
    print("Total pembayaran   : Rp " + str(total_bayar))

    valid_input = False
    while not valid_input:
        bayar_input = input("Masukkan nominal pembayaran: Rp ")

        if bayar_input == "":
            print("Input tidak boleh kosong.")
        else:
            angka = True
            for c in bayar_input:
                if c < '0' or c > '9':
                    angka = False
                    break
            if not angka:
                print("Input harus berupa angka.")
            else:
                valid_input = True

    bayar = int(bayar_input)
    if bayar >= total_bayar:
        kembalian = bayar - total_bayar
        print("Kembalian: Rp " + str(kembalian))
        print("Status: Pembayaran berhasil")
        sudah_bayar = True
    else:
        print("Nominal kurang! Pembayaran gagal.")
        sudah_bayar = False

    input("Tekan ENTER untuk kembali ke menu utama...")
    print()


def cetak_resi():
    print()
    print("=== RESI PEMESANAN ===")
    print("Film: " + booking["film"])
    print("Jam Tayang: " + booking["jam"])
    # Gabung kursi manual
    kursi_str = ""
    for i in range(len(booking["kursi"])):
        kursi_str = kursi_str + booking["kursi"][i]
        if i != len(booking["kursi"]) - 1:
            kursi_str = kursi_str + ", "
    print("Kursi: " + kursi_str)
    # Gabung makanan manual
    fnb_str = ""
    for i in range(len(pesanan_fnb)):
        fnb_str = fnb_str + pesanan_fnb[i]["nama"] + " x " + str(pesanan_fnb[i]["jumlah"])
        if i != len(pesanan_fnb) - 1:
            fnb_str = fnb_str + ", "
    print("Makanan: " + fnb_str)
    print("Total: Rp" + str(total_bayar))
    if sudah_bayar:
        print("Status: Tiket berhasil dicetak")
    else:
        print("Status: Silakan lakukan pembayaran terlebih dahulu")
    input("Tekan ENTER untuk kembali ke menu utama...")
    print()

# Main loop
while True:
    menu = tampil_menu()
    if menu == "1":
        lihat_daftar_film()
    elif menu == "2":
        booking_tiket()
    elif menu == "3":
        pesan_fnb()
    elif menu == "4":
        pembayaran()
    elif menu == "5":
        cetak_resi()
    elif menu == "6":
        print("Terima kasih sudah menggunakan layanan kami!")
        break
    else:
        print("Pilihan tidak valid!")
        print()