def pertanyaan_pilihan(pertanyaan, pilihan):
    print(pertanyaan)
    for i, (opsi, nilai, deskripsi) in enumerate(pilihan, start=1):
        print(f"{i}. {opsi} (nilai: {nilai}) - {deskripsi}")

def pilih_jurusan():
    skor = 0

    pertanyaan1 = "Apa bidang yang Anda minati?"
    pilihan1 = [
        ("Ilmu Komputer", 3, "Bidang yang berkembang pesat dalam teknologi."),
        ("Teknik", 2, "Penerapan ilmu pengetahuan dalam perancangan."),
        ("Seni dan Desain", 4, "Ekspresi kreatif dalam bentuk visual."),
        ("Ilmu Sosial", 1, "Kajian tentang perilaku sosial manusia.")
    ]
    pertanyaan_pilihan(pertanyaan1, pilihan1)
    jawaban1 = int(input("Masukkan nomor pilihan Anda: "))
    skor += pilihan1[jawaban1 - 1][1]

    pertanyaan2 = "Apa tipe pekerjaan yang Anda sukai?"
    pilihan2 = [
        ("Pekerjaan Lapangan", 2, "Aktivitas di luar ruangan dan praktis."),
        ("Pekerjaan Kantoran", 3, "Pekerjaan yang dilakukan di dalam kantor."),
        ("Pekerjaan Kreatif", 4, "Pekerjaan yang membutuhkan kreativitas dan inovasi.")
    ]
    pertanyaan_pilihan(pertanyaan2, pilihan2)
    jawaban2 = int(input("Masukkan nomor pilihan Anda: "))
    skor += pilihan2[jawaban2 - 1][1]

    pertanyaan3 = "Apakah Anda suka matematika?"
    pilihan3 = [("Ya", 2, "Memiliki dasar matematika sangat penting."),
                ("Tidak", 1, "Matematika bukan fokus utama.")]
    pertanyaan_pilihan(pertanyaan3, pilihan3)
    jawaban3 = int(input("Masukkan nomor pilihan Anda: "))
    skor += pilihan3[jawaban3 - 1][1]

    pertanyaan4 = "Apakah Anda suka berinteraksi dengan orang lain?"
    pilihan4 = [("Ya", 3, "Sosial dan suka bekerja dalam tim."),
                ("Tidak", 1, "Lebih suka bekerja sendiri.")]
    pertanyaan_pilihan(pertanyaan4, pilihan4)
    jawaban4 = int(input("Masukkan nomor pilihan Anda: "))
    skor += pilihan4[jawaban4 - 1][1]

    # Menentukan rekomendasi jurusan berdasarkan skor
    if skor >= 8:
        rekomendasi = "Ilmu Komputer"
    elif skor >= 5:
        rekomendasi = "Seni dan Desain"
    else:
        rekomendasi = "Ilmu Sosial"

    return rekomendasi

def main():
    print("Selamat datang di Sistem Pakar Pilih Jurusan!")
    nama = input("Masukkan nama Anda: ")
    print(f"Hai {nama}! Mari kita tentukan jurusan yang cocok untuk Anda.")
    
    jurusan_rekomendasi = pilih_jurusan()

    print(f"\nBerdasarkan jawaban Anda, kami merekomendasikan Anda untuk mengambil jurusan {jurusan_rekomendasi}.")

if __name__ == "__main__":
    main()
