def hitung_nakhir(uts, uas):
    return (uts + uas) / 2  # Fungsi ini menghitung nilai akhir dengan mengambil rata-rata dari UTS dan UAS.

def hitung_hmutu(nakhir):
    if nakhir < 25:
        return 'E'  # Jika nilai akhir kurang dari 25, maka mengembalikan 'E' (nilai mutu E).
    elif nakhir < 43:
        return 'D'  # Jika nilai akhir kurang dari 43, maka mengembalikan 'D' (nilai mutu D).
    elif nakhir < 60:
        return 'C'  # Jika nilai akhir kurang dari 60, maka mengembalikan 'C' (nilai mutu C).
    elif nakhir < 80:
        return 'B'  # Jika nilai akhir kurang dari 80, maka mengembalikan 'B' (nilai mutu B).
    else:
        return 'A'  # Jika nilai akhir 80 atau lebih, maka mengembalikan 'A' (nilai mutu A).

def calculate_mean(data):
    return sum(data) / len(data)  # Fungsi ini menghitung rata-rata dari data yang diberikan.

def calculate_standard_deviation(data, mean):
    squared_diff = sum((x - mean) ** 2 for x in data)
    variance = squared_diff / len(data)
    std_deviation = variance ** 0.5
    return std_deviation  # Fungsi ini menghitung simpangan baku dari data yang diberikan.

def database():
    NIM = []         # List untuk menyimpan NIM mahasiswa.
    Nama = []        # List untuk menyimpan nama mahasiswa.
    Kelompok = []    # List untuk menyimpan kelompok mahasiswa.
    UTS = []         # List untuk menyimpan nilai UTS mahasiswa.
    UAS = []         # List untuk menyimpan nilai UAS mahasiswa.
    nilaiAkhir = []  # List untuk menyimpan nilai akhir mahasiswa.
    nilaiMutu = []   # List untuk menyimpan nilai mutu mahasiswa.

    with open(r'G:\Kuliah\Komputasi Dasar\KontenGithub\tugas-komdas\NilaiUTS-UAS_prediksi.csv', 'r') as infile:
        next(infile)  # Lewati baris header pada file CSV.

        for line in infile:
            data = line.strip().split(',')  # Membaca data per baris dan memisahkan kolom dengan tanda koma.
            NIM.append(data[0])
            Nama.append(data[1])
            Kelompok.append(data[2])
            UTS.append(int(data[3]))
            UAS.append(int(data[4]))
            nilai_akhir = hitung_nakhir(UTS[-1], UAS[-1])  # Menghitung nilai akhir untuk mahasiswa saat ini.
            nilaiAkhir.append(nilai_akhir)
            nilaiMutu.append(hitung_hmutu(nilai_akhir))  # Menghitung nilai mutu berdasarkan nilai akhir.

    return NIM, Nama, Kelompok, UTS, UAS, nilaiAkhir, nilaiMutu

def hasilData():
    NIM, Nama, Kelompok, UTS, UAS, nilaiAkhir, nilaiMutu = database()

    def print_row(index, nim, Nama, kelompok, uts, uas, nilai_akhir, huruf_mutu):
        print(f"{index:3} | {nim:12} | {Nama:40}  | {kelompok:8} | {uts:3} | {uas:3}   | {nilai_akhir:8.2f}    |   {huruf_mutu}        |")
    
    print("=" * 123)
    print("| No |      NIM      |                 Nama                    | Kelompok |  UTS |  UAS | Nilai Akhir | Huruf Mutu |")
    print("=" * 123)

    for i in range(len(NIM)):
        print_row(i + 1, NIM[i], Nama[i], Kelompok[i], UTS[i], UAS[i], nilaiAkhir[i], nilaiMutu[i])
    print("=" * 123)

def daftarFakultas():
    NIM, _, _, UTS, UAS, nilaiAkhir, nilaiMutu = database()

    fakultas_counts = {}                 # Dictionary untuk menghitung jumlah mahasiswa per fakultas.
    fakultas_nilai = {}                  # Dictionary untuk menghitung total nilai akhir per fakultas.
    fakultas_nilai_rounded = {}          # Dictionary untuk menyimpan rata-rata nilai akhir per fakultas (dibulatkan).
    fakultas_std_deviation = {}           # Dictionary untuk menyimpan simpangan baku per fakultas.
    
    uts_values = []                       # List untuk menyimpan nilai-nilai UTS semua mahasiswa.
    uas_values = []                       # List untuk menyimpan nilai-nilai UAS semua mahasiswa.
    nilai_akhir_values = []               # List untuk menyimpan nilai akhir semua mahasiswa.

    fakultas_names = {
        'A': 'Fakultas Pertanian',
        'B': 'Fakultas Kehutanan',
        'C': 'Fakultas Perikanan dan Ilmu Kelautan',
        'D': 'Fakultas Peternakan',
        'E': 'Fakultas Teknologi Pertanian',
        'F': 'Fakultas Matematika dan Ilmu Pengetahuan Alam',
        'G': 'Fakultas Ekonomi dan Manajemen',
        'H': 'Fakultas Ekologi Manusia',
        'I': 'Fakultas Tambahan',
    }

    huruf_mutu_counts = {}                # Dictionary untuk menghitung jumlah mahasiswa per huruf mutu.

    for i in range(len(NIM)):
        fakultas = NIM[i][0]  # Mengambil kode fakultas dari NIM mahasiswa.
        if fakultas not in fakultas_counts:
            fakultas_counts[fakultas] = 0
            fakultas_nilai[fakultas] = 0
            fakultas_std_deviation[fakultas] = []

        fakultas_counts[fakultas] += 1
        fakultas_nilai[fakultas] += nilaiAkhir[i]

        uts_values.append(UTS[i])
        uas_values.append(UAS[i])
        nilai_akhir_values.append(nilaiAkhir[i])

        fakultas_std_deviation[fakultas].append(nilaiAkhir[i])

        # Menghitung jumlah mahasiswa per huruf mutu
        huruf = nilaiMutu[i]
        if huruf not in huruf_mutu_counts:
            huruf_mutu_counts[huruf] = 0
        huruf_mutu_counts[huruf] += 1

    for fakultas, count in fakultas_counts.items():
        fakultas_nilai_rounded[fakultas] = round(fakultas_nilai[fakultas] / count, 2)  # Menyimpan rata-rata nilai akhir per fakultas (dibulatkan).

    uts_mean = calculate_mean(uts_values)                  # Menghitung rata-rata nilai UTS semua mahasiswa.
    uas_mean = calculate_mean(uas_values)                  # Menghitung rata-rata nilai UAS semua mahasiswa.
    nilai_akhir_mean = calculate_mean(nilai_akhir_values)  # Menghitung rata-rata nilai akhir semua mahasiswa.
    
    uts_stddev = calculate_standard_deviation(uts_values, uts_mean)             # Menghitung simpangan baku nilai UTS.
    uas_stddev = calculate_standard_deviation(uas_values, uas_mean)             # Menghitung simpangan baku nilai UAS.
    nilai_akhir_stddev = calculate_standard_deviation(nilai_akhir_values, nilai_akhir_mean)  # Menghitung simpangan baku nilai akhir.

    # Menghitung Indeks Prestasi (IP) per fakultas
    ip_per_fakultas = {}
    total_mahasiswa = sum(fakultas_counts.values())
    for fakultas, count in fakultas_counts.items():
        total_bobot = 0
        for i in range(len(NIM)):
            if NIM[i][0] == fakultas:
                huruf_mutu = nilaiMutu[i]
                bobot = 4 if huruf_mutu == 'A' else 3 if huruf_mutu == 'B' else 2 if huruf_mutu == 'C' else 1 if huruf_mutu == 'D' else 0
                total_bobot += bobot
        ip = total_bobot / count
        ip_per_fakultas[fakultas] = round(ip, 2)  # Menyimpan IP per fakultas (dibulatkan ke 2 desimal).

    # Membuat format string untuk header tabel
    spaces = "\n" * 3
    header = "| {:<60} | {:<20} | {:<20} | {:<20} | {:<40} | {:<40} |\n".format("Fakultas", "Jumlah Mahasiswa", "Total Nilai Akhir", "Simpangan Baku", "Rata-Rata Fakultas", "IP")
    separator = "=" * 219 + "\n"

    # Membuat format string untuk baris tabel data fakultas
    data_rows = ""
    huruf_mutu_stats = ""
    for fakultas in fakultas_counts.keys():
        std_dev = calculate_standard_deviation(fakultas_std_deviation[fakultas], calculate_mean(fakultas_std_deviation[fakultas]))
        data_row = "| {:<60} | {:<20} | {:<20} | {:<20} | {:<40} | {:<40} |\n".format(fakultas_names[fakultas], fakultas_counts[fakultas], fakultas_nilai[fakultas], round(std_dev, 2), fakultas_nilai_rounded[fakultas], ip_per_fakultas[fakultas])
        data_rows += data_row

    # Membuat format string untuk statistik jumlah mahasiswa per huruf mutu
    huruf_mutu_stats += "| Statistik jumlah mahasiswa per Huruf Mutu : {:<100} |\n".format("Nilai Akhir")
    for huruf, count in huruf_mutu_counts.items():
        huruf_mutu_stats += "| {:<2} : {:<4} | {:<62} |\n".format(huruf, count, " ".join(map(str, nilaiMutu)))

    # Menggabungkan semua format string
    result_table = spaces + separator + header + separator + data_rows + separator

    # Mencetak tabel hasil
    print(result_table)

def tabelDistribusiNilaiMutuPerFakultas():
    NIM, _, _, _, _, _, nilaiMutu = database()

    fakultas_names = {
        'A': 'Fakultas Pertanian',
        'B': 'Fakultas Kehutanan',
        'C': 'Fakultas Perikanan dan Ilmu Kelautan',
        'D': 'Fakultas Peternakan',
        'E': 'Fakultas Teknologi Pertanian',
        'F': 'Fakultas Matematika dan Ilmu Pengetahuan Alam',
        'G': 'Fakultas Ekonomi dan Manajemen',
        'H': 'Fakultas Ekologi Manusia',
        'I': 'Fakultas Tambahan',
    }

    # Membuat format string untuk header tabel
    spaces = "\n" * 3
    header = "| {:<60} | {:<1} | {:<1} | {:<1} | {:<1} | {:<1} |\n".format("Fakultas", "A", "B", "C", "D", "E")
    separator = "=" * 85 + "\n"

    # Menyimpan distribusi nilai mutu per fakultas
    distribusi_nilai_mutu = {}
    
    for fakultas in fakultas_names.keys():
        distribusi_nilai_mutu[fakultas] = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

    for i in range(len(NIM)):
        fakultas = NIM[i][0]
        grade = nilaiMutu[i]
        distribusi_nilai_mutu[fakultas][grade] += 1

    # Membuat format string untuk baris tabel distribusi nilai mutu per fakultas
    data_rows = ""
    for fakultas, grade_counts in distribusi_nilai_mutu.items():
        grade_counts_str = " | ".join([str(grade_counts[grade]) for grade in "ABCDE"])
        data_row = "| {:<60} | {} |\n".format(fakultas_names[fakultas], grade_counts_str)
        data_rows += data_row

    # Menggabungkan format string untuk tabel distribusi nilai mutu per fakultas
    result_table = spaces + separator + header + separator + data_rows + separator

    # Mencetak tabel hasil
    print(result_table)

# Panggil fungsi untuk menampilkan tabel distribusi nilai mutu per fakultas
hasilData()
daftarFakultas()
tabelDistribusiNilaiMutuPerFakultas()
