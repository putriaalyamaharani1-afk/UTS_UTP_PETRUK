def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                try:
                    npm, nama, nilai = baris.strip().split(";")
                    data.append({"npm": npm, "nama": nama, "nilai": int(nilai)})
                except ValueError:
                    continue  # baris rusak dilewati
    except FileNotFoundError:
        print("File nilai.txt belum ada")
    return data
