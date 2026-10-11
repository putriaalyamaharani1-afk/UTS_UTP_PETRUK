# katalog/fileio.py

def buat_file(nama_file):
    # mode x: 
    try:
        with open(nama_file, "x") as file:
            print("File berhasil dibuat!")
    except FileExistsError:
        print("File sudah ada")


def tambah_film(nama_file, judul, genre, tahun, rating):
    # mode a:
    with open(nama_file, "a") as file:
        file.write(f"{judul};{genre};{tahun};{rating}\n")


def baca_film(nama_file):
    # mode r: 
    data = []
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                try:
                    judul, genre, tahun, rating = baris.strip().split(";")
                    data.append({
                        "judul": judul,
                        "genre": genre,
                        "tahun": int(tahun),
                        "rating": int(rating),
                    })
                except ValueError:
                    continue  # baris rusak dilewati
    except FileNotFoundError:
        print(f"File {nama_file} belum ada")
    return data


def tulis_laporan(isi, nama_file="laporan_film.txt"):
    # mode w: 
    with open(nama_file, "w") as file:
        file.write(isi)