def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                hari, suhu = baris.strip().split(";")
                data.append({"hari": hari, "suhu": int(suhu)})
    except FileNotFoundError:
        print("File tidak ditemukan")
    return data


def hitung_rata_rata(*args):
    return sum(args) / len(args)


def tentukan_kategori(suhu, batas=32):
    if suhu >= batas:
        return "Panas"
    return "Normal"


def analisis(data):
    suhu_semua = [d["suhu"] for d in data]
    rata_rata = hitung_rata_rata(*suhu_semua)
    tertinggi = max(data, key=lambda d: d["suhu"])
    terendah = min(data, key=lambda d: d["suhu"])
    for d in data:
        d["kategori"] = tentukan_kategori(suhu=d["suhu"])
    jumlah_panas = len([d for d in data if d["kategori"] == "Panas"])
    return rata_rata, tertinggi, terendah, jumlah_panas


def tulis_laporan(data, hasil):
    rata_rata, tertinggi, terendah, jumlah_panas = hasil
    with open("laporan_suhu.txt", "w") as file:
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Tertinggi: {tertinggi['suhu']} ({tertinggi['hari']})\n")
        file.write(f"Terendah: {terendah['suhu']} ({terendah['hari']})\n")
        for d in data:
            file.write(f"{d['hari']}: {d['suhu']} - {d['kategori']}\n")
        file.write(f"Jumlah hari Panas: {jumlah_panas}\n")
    with open("laporan_suhu.txt", "r") as file:
        print(file.read())


if __name__ == "__main__":
    data = baca_data("suhu.txt")
    hasil = analisis(data)
    tulis_laporan(data, hasil)