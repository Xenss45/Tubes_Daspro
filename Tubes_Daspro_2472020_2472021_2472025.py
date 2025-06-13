movies = [
    [1, "Avengers: Endgame", 50],
    [2, "Inception", 40],
    [3, "Interstellar", 30],
    [4, "The Batman", 25]
]

TICKET_PRICE = 30000  
DISCOUNT_THRESHOLD = 5  
DISCOUNT_RATE = 0.1  

seats = {i: ["[ ]"] * movies[i-1][2] for i in range(1, len(movies) + 1)}  

tickets = [None] * 100  
ticket_count = 0       

def is_number(s):
    for char in s:
        if char < '0' or char > '9':
            return False
    return True

def input_number(prompt):
    while True:
        value = input(prompt)
        if is_number(value):
            return int(value)
        print("❌ Input harus berupa angka. Silakan coba lagi.")

def show_movies():
    print("--- Daftar Film ---")
    for movie in movies:
        print(f"{movie[0]}. {movie[1]} ({sum(1 for seat in seats[movie[0]] if seat == '[ ]')} kursi tersedia)")

def show_seats(movie_id):
    print(f"Kursi untuk {movies[movie_id-1][1]}")
    print(" ".join(seats[movie_id]))

def order_ticket():
    global ticket_count
    show_movies()

    movie_id = input_number("Masukkan ID film yang ingin dipesan: ")

    if movie_id < 1 or movie_id > len(movies):
        print("❌ Film tidak ditemukan. Silakan coba lagi.")
        return

    name = input("Masukkan nama Anda: ")

    available_seats = sum(1 for seat in seats[movie_id] if seat == "[ ]")

    number = input_number("Jumlah tiket: ")

    if number <= 0 or number > available_seats:
        print("❌ Jumlah tiket tidak valid. Silakan coba lagi.")
        return

    total_price = number * TICKET_PRICE
    if number > DISCOUNT_THRESHOLD:
        total_price *= (1 - DISCOUNT_RATE)
        print(f" Anda mendapatkan diskon 10%! Total harga setelah diskon: Rp{total_price}")

    show_seats(movie_id)
    chosen_seats = []
    for i in range(number):
        while True:
            seat_num = input_number(f"Pilih kursi {i+1} (0-{len(seats[movie_id])-1}): ")  # Tetap gunakan panjang seats[movie_id]
            if seat_num >= 0 and seat_num < len(seats[movie_id]) and seats[movie_id][seat_num] == "[ ]":
                break
            print("❌ Kursi tidak valid atau sudah dipesan. Silakan coba lagi.")
        chosen_seats.append(seat_num)

    for seat in chosen_seats:
        seats[movie_id][seat] = "[X]"

    tickets[ticket_count] = [name, movies[movie_id-1][1], number, total_price, chosen_seats]
    ticket_count += 1

    print(f"✅ Tiket berhasil dipesan! Total harga: Rp{total_price}")

def view_tickets():
    print("--- Daftar Pemesanan ---")
    if ticket_count == 0 or all(t is None for t in tickets[:ticket_count]):
        print("Belum ada pemesanan.")
    else:
        for i in range(ticket_count):
            if tickets[i] is not None:
                print(f"{i+1}. {tickets[i][0]} memesan {tickets[i][2]} tiket untuk '{tickets[i][1]}' - Total: Rp{tickets[i][3]} - Kursi: {tickets[i][4]}")

def cancel_ticket():
    global ticket_count
    view_tickets()
    if ticket_count == 0:
        return

    index = input_number("Masukkan nomor pesanan yang ingin dibatalkan: ") - 1

    if index < 0 or index >= ticket_count or tickets[index] is None:
        print("❌ Nomor pesanan tidak valid. Silakan coba lagi.")
        return

    cancelled = tickets[index]
    tickets[index] = None

    movie_id = next(i + 1 for i in range(len(movies)) if movies[i][1] == cancelled[1])
    for seat in cancelled[4]:
        seats[movie_id][seat] = "[ ]"

    print(f"❌ Pemesanan berhasil dibatalkan. Uang dikembalikan: Rp{cancelled[3]}")

def main():
    while True:
        print("===== Aplikasi Tiket Bioskop =====")
        print("1. Lihat daftar film")
        print("2. Pesan tiket")
        print("3. Lihat daftar pemesanan")
        print("4. Batalkan pemesanan")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            show_movies()
        elif pilihan == "2":
            order_ticket()
        elif pilihan == "3":
            view_tickets()
        elif pilihan == "4":
            cancel_ticket()
        elif pilihan == "5":
            total_income = sum(int(t[3]) for t in tickets if t is not None)
            print(f"Total pendapatan dari semua tiket yang masih aktif: Rp{total_income}")
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()