import unittest
from suhu import hitung_rata_rata, tentukan_kategori

class TestSuhu(unittest.TestCase):
    def test_rata_rata(self):
        self.assertEqual(hitung_rata_rata(30, 32, 34), 32)

    def test_panas(self):
        self.assertEqual(tentukan_kategori(32), "Panas")

    def test_normal(self):
        self.assertEqual(tentukan_kategori(31), "Normal")

if __name__ == "__main__":
    unittest.main()