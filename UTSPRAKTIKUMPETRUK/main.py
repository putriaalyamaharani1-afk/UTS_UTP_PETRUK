# main.py
from katalog import (buat_file, tambah_film, baca_film, tulis_laporan,
                     KatalogFilm, cek_judul, cek_rating, cek_tahun, DataFilmError)

NAMA_FILE = "film.txt"   # nama file data, cukup ditulis sekali

while True:
    print("\n1. Buat file  2. Tambah film  3. Tampilkan  4. Laporan  5. Keluar")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        buat_file(NAMA_FILE)                       # mode x

    elif pilihan == "2":
        try:
            judul = cek_judul(input("Judul: "))
            genre = input("Genre: ").lower()
            tahun = cek_tahun(input("Tahun: "))
            rating = cek_rating(input("Rating (1-10): "))
            tambah_film(NAMA_FILE, judul, genre, tahun, rating)   # mode a
            print("Film ditambahkan")
        except DataFilmError as e:
            print("Gagal:", e)

    elif pilihan == "3":
        katalog = KatalogFilm(baca_film(NAMA_FILE))                # mode r
        for f in katalog.urutkan_rating():
            print(f.info())

    elif pilihan == "4":
        katalog = KatalogFilm(baca_film(NAMA_FILE))
        isi = f"Jumlah film: {len(katalog.daftar_film)}\n"
        isi += f"Rata-rata rating: {katalog.rata_rata_rating():.2f}\n"
        for f in katalog.filter_genre(genre="drama"):              # keyword argument
            isi += f"- {f.info()}\n"
        tulis_laporan(isi)                                         # mode w
        print(isi)

    elif pilihan == "5":
        break