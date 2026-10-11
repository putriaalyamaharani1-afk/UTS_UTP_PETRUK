BATAS_KELULUSAN = 70

def hitung_rata_rata(*args):
    return sum(args) / len(args)

def tentukan_status_kelulusan(rata_rata, batas_lulus=BATAS_KELULUSAN):
    return "Lulus" if rata_rata >= batas_lulus else "Tidak Lulus"

def tampilkan_hasil(nama, rata_rata, status):
    print(f"nama : {nama}")
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Status Kelulusan: {status}")
    
#dujalankan langsung
if __name__ == "__main__":
    rata_rata_budi = hitung_rata_rata(80, 90, 75)
    status_budi = tentukan_status_kelulusan(rata_rata_budi)
    tampilkan_hasil("Budi", rata_rata_budi, status_budi)
