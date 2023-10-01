# Fungsi ini menghitung nilai akhir mahasiswa berdasarkan nilai UTS dan UAS.
def calculate_final_score(midterm, final):
    return (midterm + final) / 2

# Fungsi ini menentukan huruf mutu berdasarkan nilai akhir.
def determine_grade(final_score):
    if final_score < 25:
        return 'E'  # Mengembalikan nilai 'E' jika nilai akhir kurang dari 25.
    elif final_score < 43:
        return 'D'  # Mengembalikan nilai 'D' jika nilai akhir kurang dari 43.
    elif final_score < 60:
        return 'C'  # Mengembalikan nilai 'C' jika nilai akhir kurang dari 60.
    elif final_score < 80:
        return 'B'  # Mengembalikan nilai 'B' jika nilai akhir kurang dari 80.
    else:
        return 'A'  # Mengembalikan nilai 'A' jika nilai akhir 80 atau lebih.

# Fungsi ini menghitung rata-rata dari data yang diberikan.
def calculate_mean(data):
    return sum(data) / len(data)

# Fungsi ini menghitung simpangan baku dari data yang diberikan.
def calculate_standard_deviation(data, mean):
    squared_diff = sum((x - mean) ** 2 for x in data)
    variance = squared_diff / len(data)
    std_deviation = variance ** 0.5
    return std_deviation

# Fungsi ini membaca data mahasiswa dari file CSV.
def read_student_data(file_path):
    student_data = []

    with open(file_path, 'r') as infile:
        next(infile)  # Lewati baris header pada file CSV.

        for line in infile:
            data = line.strip().split(',')  # Membaca data per baris dan memisahkan kolom dengan tanda koma.
            final_score = calculate_final_score(int(data[3]), int(data[4]))  # Menghitung nilai akhir untuk mahasiswa saat ini.
            grade = determine_grade(final_score)  # Menentukan huruf mutu berdasarkan nilai akhir.
            student_data.append({
                'NIM': data[0],
                'Nama': data[1],
                'Kelompok': data[2],
                'UTS': int(data[3]),
                'UAS': int(data[4]),
                'Nilai Akhir': final_score,
                'Huruf Mutu': grade
            })

    return student_data

# Fungsi ini mencetak data mahasiswa ke dalam tabel.
def print_student_data(student_data):
    print("=" * 123)
    print("| No |      NIM      |                 Nama                    | Kelompok |  UTS |  UAS | Nilai Akhir | Huruf Mutu |")
    print("=" * 123)

    for i, data in enumerate(student_data, start=1):
        print(f"{i:3} | {data['NIM']:12} | {data['Nama']:40}  | {data['Kelompok']:8} | {data['UTS']:3} | {data['UAS']:3}   | {data['Nilai Akhir']:8.2f}    |   {data['Huruf Mutu']}        |")
    
    print("=" * 123)

# Fungsi ini menghitung statistik per fakultas.
def calculate_statistics(student_data):
    faculty_counts = {}
    faculty_scores = {}
    faculty_std_deviation = {}

    for data in student_data:
        faculty = data['NIM'][0]  # Mengambil kode fakultas dari NIM mahasiswa.

        if faculty not in faculty_counts:
            faculty_counts[faculty] = 0
            faculty_scores[faculty] = 0
            faculty_std_deviation[faculty] = []

        faculty_counts[faculty] += 1
        faculty_scores[faculty] += data['Nilai Akhir']

        faculty_std_deviation[faculty].append(data['Nilai Akhir'])

    faculty_means = {faculty: faculty_scores[faculty] / count for faculty, count in faculty_counts.items()}  # Menghitung rata-rata nilai akhir per fakultas.
    faculty_std_dev = {faculty: calculate_standard_deviation(data, faculty_means[faculty]) for faculty, data in faculty_std_deviation.items()}  # Menghitung simpangan baku per fakultas.

    return faculty_counts, faculty_scores, faculty_std_dev, faculty_means

# Fungsi ini mencetak statistik per fakultas ke dalam tabel.
def print_faculty_statistics(faculty_counts, faculty_scores, faculty_std_dev, faculty_means):
    faculty_names = {
        'A': 'Fakultas Pertanian',
        'B': 'Sekolah Kedokteran Hewan dan Biomedis',
        'C': 'Fakultas Perikanan dan Ilmu Kelautan',
        'D': 'Fakultas Peternakan',
        'E': 'Fakultas Kehutanan dan Lingkungan',
        'F': 'Fakultas Teknologi Pertanian',
        'G': 'Fakultas Matematika dan Ilmu Pengetahuan Alam',
        'H': 'Fakultas Ekonomi dan Manajemen',
        'I': 'Fakultas Ekologi Manusia',
    }

    print("=" * 219)
    print("| {:<60} | {:<20} | {:<20} | {:<20} | {:<40} | {:<40} |".format("Fakultas", "Jumlah Mahasiswa", "Total Nilai Akhir", "Simpangan Baku", "Rata-Rata Fakultas", "IP"))
    print("=" * 219)

    for faculty in faculty_counts.keys():
        std_dev = faculty_std_dev[faculty]
        print("| {:<60} | {:<20} | {:<20} | {:<20} | {:<40} | {:<40} |".format(faculty_names[faculty], faculty_counts[faculty], faculty_scores[faculty], round(std_dev, 2), round(faculty_means[faculty], 2), round(faculty_means[faculty] / 25, 2)))  # IP dihitung dengan membagi rata-rata nilai akhir per fakultas dengan 25.
    
    print("=" * 219)

# Fungsi ini menghitung distribusi nilai mutu per fakultas.
def calculate_grade_distribution(student_data):
    faculty_names = {
        'A': 'Fakultas Pertanian',
        'B': 'Sekolah Kedokteran Hewan dan Biomedis',
        'C': 'Fakultas Perikanan dan Ilmu Kelautan',
        'D': 'Fakultas Peternakan',
        'E': 'Fakultas Kehutanan dan Lingkungan',
        'F': 'Fakultas Teknologi Pertanian',
        'G': 'Fakultas Matematika dan Ilmu Pengetahuan Alam',
        'H': 'Fakultas Ekonomi dan Manajemen',
        'I': 'Fakultas Ekologi Manusia',
    }

    grade_distribution = {}

    for faculty in faculty_names.keys():
        grade_distribution[faculty] = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

    for data in student_data:
        faculty = data['NIM'][0]
        grade = data['Huruf Mutu']
        grade_distribution[faculty][grade] += 1

    return grade_distribution

# Fungsi ini mencetak distribusi nilai mutu per fakultas ke dalam tabel.
def print_grade_distribution(grade_distribution):
    print("=" * 85)
    print("| {:<60} | {:<1} | {:<1} | {:<1} | {:<1} | {:<1} |".format("Fakultas", "A", "B", "C", "D", "E"))
    print("=" * 85)

    faculty_names = {
        'A': 'Fakultas Pertanian',
        'B': 'Sekolah Kedokteran Hewan dan Biomedis',
        'C': 'Fakultas Perikanan dan Ilmu Kelautan',
        'D': 'Fakultas Peternakan',
        'E': 'Fakultas Kehutanan dan Lingkungan',
        'F': 'Fakultas Teknologi Pertanian',
        'G': 'Fakultas Matematika dan Ilmu Pengetahuan Alam',
        'H': 'Fakultas Ekonomi dan Manajemen',
        'I': 'Fakultas Ekologi Manusia',
    }

    for faculty in faculty_names.keys():
        grade_counts = grade_distribution[faculty]
        grade_counts_str = " | ".join([str(grade_counts[grade]) for grade in "ABCDE"])
        print("| {:<60} | {} |".format(faculty_names[faculty], grade_counts_str))

    print("=" * 85)

# Fungsi utama program.
def main():
    file_path = r'Lokasi-File-Nya-Di-Laptop-Kamu\NilaiUTS-UAS_prediksi.csv'  # Ganti dengan lokasi file CSV Kamu.
    student_data = read_student_data(file_path)

    print_student_data(student_data)

    faculty_counts, faculty_scores, faculty_std_dev, faculty_means = calculate_statistics(student_data)
    print_faculty_statistics(faculty_counts, faculty_scores, faculty_std_dev, faculty_means)

    grade_distribution = calculate_grade_distribution(student_data)
    print_grade_distribution(grade_distribution)

if __name__ == "__main__":
    main()
