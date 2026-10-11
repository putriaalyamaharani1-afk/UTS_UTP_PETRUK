class film:
    def __init__(self, **kwargs):
        self.judul = kwargs.get("judul")
        self.genre = kwargs.get("genre")
        self.tahun = kwargs.get("tahun")
        self.rating = kwargs.get("rating")

    def info(self):
        return f"{self.judul} ({self.tahun}) - {self.genre} - Rating: {self.rating}"
    
# katalog/processing.py

class Film:
    def __init__(self, **kwargs):
        # **kwargs: terima data film dalam bentuk key=value
        self.judul = kwargs["judul"]
        self.genre = kwargs["genre"]
        self.tahun = kwargs["tahun"]
        self.rating = kwargs["rating"]

    def info(self):
        return f"{self.judul} ({self.tahun}) - {self.genre} - rating {self.rating}"


class KatalogFilm:
    def __init__(self, data):
        # ubah list of dictionary menjadi list objek Film
        self.daftar_film = []
        for d in data:
            self.daftar_film.append(Film(**d))

    def hitung_rata_rata(self, *args):
        # *args: jumlah rating bebas
        return sum(args) / len(args)

    def rata_rata_rating(self):
        semua_rating = [f.rating for f in self.daftar_film]
        return self.hitung_rata_rata(*semua_rating)

    def filter_genre(self, genre):
        # lambda sebagai syarat filter
        return list(filter(lambda f: f.genre == genre, self.daftar_film))

    def urutkan_rating(self):
        # lambda sebagai key pengurutan
        return sorted(self.daftar_film, key=lambda f: f.rating, reverse=True)

    def film_terbaru(self):
        return max(self.daftar_film, key=lambda f: f.tahun)