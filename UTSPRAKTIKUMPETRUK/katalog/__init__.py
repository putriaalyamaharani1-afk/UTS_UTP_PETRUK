# katalog/__init__.py
# menandai folder ini sebagai package, dan mengekspor fungsi/class utama
from .fileoi import buat_file, tambah_film, baca_film, tulis_laporan
from .proses import Film, KatalogFilm
from .validasi import cek_judul, cek_rating, cek_tahun, DataFilmError