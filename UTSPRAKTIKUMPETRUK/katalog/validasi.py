# katalog/validasi.py

class DataFilmError(Exception):
    # exception buatan sendiri untuk data film yang tidak valid
    pass


def cek_judul(judul):
    # raise: munculkan error buatan sendiri kalau judul kosong
    if judul.strip() == "":
        raise DataFilmError("Judul tidak boleh kosong")
    return judul


def cek_rating(rating):
    # try/except: ubah teks jadi angka, tangkap ValueError kalau bukan angka
    try:
        rating = int(rating)
    except ValueError:
        raise DataFilmError("Rating harus berupa angka")
    # raise: rating di luar rentang 1-10 tidak valid
    if rating < 1 or rating > 10:
        raise DataFilmError("Rating harus antara 1 sampai 10")
    return rating


def cek_tahun(tahun):
    # ubah tahun jadi angka, tahun negatif atau nol tidak valid
    try:
        tahun = int(tahun)
    except ValueError:
        raise DataFilmError("Tahun harus berupa angka")
    if tahun <= 0:
        raise
    
def cek_tahun(tahun):
    # ubah tahun jadi angka, tahun nol atau negatif tidak valid
    try:
        tahun = int(tahun)
    except ValueError:
        raise DataFilmError("Tahun harus berupa angka")
    if tahun <= 0:
        raise DataFilmError("Tahun harus lebih dari 0")
    return tahun