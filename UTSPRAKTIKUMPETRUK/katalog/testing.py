# katalog/testing.py
import unittest
from proses import Film, KatalogFilm
from validasi import cek_rating, cek_judul, DataFilmError

# data contoh untuk pengujian (tidak membaca file)
DATA = [
    {"judul": "A", "genre": "drama", "tahun": 2020, "rating": 8},
    {"judul": "B", "genre": "aksi", "tahun": 2022, "rating": 6},
    {"judul": "C", "genre": "drama", "tahun": 2018, "rating": 10},
]


class TestKatalog(unittest.TestCase):
    def setUp(self):
        # dijalankan sebelum tiap pengujian: buat katalog baru
        self.katalog = KatalogFilm(DATA)

    def test_rata_rata_rating(self):
        # (8 + 6 + 10) / 3 = 8
        self.assertEqual(self.katalog.rata_rata_rating(), 8)

    def test_filter_genre(self):
        # hanya 2 film drama
        hasil = self.katalog.filter_genre(genre="drama")
        self.assertEqual(len(hasil), 2)

    def test_urutkan_rating(self):
        # rating tertinggi (10) ada di urutan pertama
        self.assertEqual(self.katalog.urutkan_rating()[0].judul, "C")

    def test_film_terbaru(self):
        # tahun terbesar adalah 2022 (film B)
        self.assertEqual(self.katalog.film_terbaru().judul, "B")

    def test_rating_tidak_valid(self):
        # rating 15 di luar 1-10, harus memunculkan DataFilmError
        with self.assertRaises(DataFilmError):
            cek_rating(15)

    def test_judul_kosong(self):
        # judul kosong harus memunculkan DataFilmError
        with self.assertRaises(DataFilmError):
            cek_judul("")


if __name__ == "__main__":
    unittest.main()