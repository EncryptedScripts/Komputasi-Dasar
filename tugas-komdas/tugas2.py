import random
# di sini saya mengimport modul random untuk membuat angka random yang nanti akan dimasukkan ke dalam array

# di sini saya membuat fungsi menu


def Menu():
    # di sini saya membuat print menu yang akan dipilih berupa menu 1 dan 2
    print("1) Start!")
    print("2) Exit")
    # pilihan tersebut nanti akan dibaca sebagai string yang nanti akan masuk ke dalam variabel choice
    choice = str(input("Select one: "))
    # return choice adalah agar fungsi menu ini dapat mengembalikan nilai choice
    return choice

# di sini saya membuat fungsi arrays


def arrays():
    # di sini saya membuat array kosong
    my_array = []
    # di sini saya membuat inputan untuk panjang array yang di simpan dalam variabel x
    # saya menggunakan try dan except untuk menangkap error jika user menginputkan selain integer
    try:
        x = int(input("Enter the length of array: "))
        # pada perkondisian ini saya lakukan agar dapat menghasilkan error jika user menginputkan nilai selain integer positif yang nanti akan ditangkap oleh except
        if (x <= 0):
            # saya menggunakan raise ValueError untuk menangkap error jika user menginputkan nilai selain integer positif
            raise ValueError
    # di sini pada except ValueError akan menangkap error jika user menginputkan nilai selain integer positif dan menghasilkan print "Please enter a positive integer" dan mengembalikan pada fungsi arrays
    except ValueError:
        print("Please enter a positive integer")
        return arrays()
    # di sini saya membuat perulangan untuk mengisi array dengan jumlah pengulangan sebanyak nilai x yang diinputkan
    for i in range(x):
        # di sini saya menggunakan fungsi append untuk menambahkan angka random ke dalam array kosong dari range 0 sampai 100
        my_array.append(random.randint(0, 100))
    # di sini saya membuat variabel minimum dan maximum yang diisi dengan nilai dari index 0 dari array
    minimum = my_array[0]
    maximum = my_array[0]
    # di sini saya membuat variabel summary yang diisi dengan 0
    summary = 0
    # di sini saya membuat perulangan untuk mencari nilai minimum, maximum, dan summary dari array yang dimana nilai pengulangan sebanyak panjang array
    for num in my_array:
        # jika num lebih kecil dari nilai minimum maka nilai minimum akan diisi dengan nilai num
        if num < minimum:
            minimum = num
        # jika num lebih besar dari nilai maximum maka nilai maximum akan diisi dengan nilai num
        if num > maximum:
            maximum = num
        # di sini saya membuat summary yang diisi dengan summary ditambah dengan nilai num untuk mencari nilai summary dari array
        summary += num
    # di sini saya membuat variabel length yang diisi dengan panjang array
    length = len(my_array)
    # di sini saya membuat variabel average yang diisi dengan nilai summary dibagi dengan panjang array
    average = summary / length
    # di sini saya membuat print array, minimum, maximum, summary, length, dan average
    print("My_Array:", my_array)
    print("====================================")
    print("The minimum number of this array is:", minimum)
    print("====================================")
    print("The maximum number of this array is:", maximum)
    print("====================================")
    print("The summary of this array is:", summary)
    print("====================================")
    print("The length of this array is:", length)
    print("====================================")
    print("The average of this array is:", average)
    print("====================================")

    # di sini saya mendeklarasikan variabel a, b, c, d, e, f, g, h, z, j yang diisi dengan 0 berfungsi untuk menghitung banyaknya data per range maksudnya yang nanti akan diprint bintang sebanyak nilai tertentu yang muncul pada array
    a, b, c, d, e, f, g, h, z, j = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    # di sini saya membuat pengulanagn untuk mencetak index dan bintang sebanyak nilai dari index array
    for i in range(len(my_array)):
        # di sini saya membuat print index dan bintang sebanyak nilai dari index array

        # saya menambahkan beberapa logic untuk print bintang sebanyak nilai dari index array, contoh jika nilai dari array yang ada pada index dari range 0 sampai 10 ada sebanyak 4 index maka akan mencetak bintang sebanyak 4
        # kurang lebih seperti itu logicnya
        if (my_array[i] >= 0 and my_array[i] <= 10):
            a += 1
        elif (my_array[i] >= 11 and my_array[i] <= 20):
            b += 1
        elif (my_array[i] >= 21 and my_array[i] <= 30):
            c += 1
        elif (my_array[i] >= 31 and my_array[i] <= 40):
            d += 1
        elif (my_array[i] >= 41 and my_array[i] <= 50):
            e += 1
        elif (my_array[i] >= 51 and my_array[i] <= 60):
            f += 1
        elif (my_array[i] >= 61 and my_array[i] <= 70):
            g += 1
        elif (my_array[i] >= 71 and my_array[i] <= 80):
            h += 1
        elif (my_array[i] >= 81 and my_array[i] <= 90):
            z += 1
        elif (my_array[i] >= 91 and my_array[i] <= 100):
            j += 1

    # di sini saya membuat print banyaknya data per range dan bintang sebanyak nilai dari index array
    print("0-10:", "*"*a)
    print("11-20:", "*"*b)
    print("21-30:", "*"*c)
    print("31-40:", "*"*d)
    print("41-50:", "*"*e)
    print("51-60:", "*"*f)
    print("61-70:", "*"*g)
    print("71-80:", "*"*h)
    print("81-90:", "*"*z)
    print("91-100:", "*"*j)

    # ini hanyalah sebuah border
    print("====================================")


# di sini saya menggunakan perulangan while true agar program dapat berjalan terus menerus
while True:
    # di sini saya membuat variabel menuss yang diisi dengan fungsi menu
    menuss = Menu()
    # jika menuss sama dengan 1 maka akan memanggil fungsi arrays
    if menuss == "1":
        arrays()
    # selain itu jika menuss sama dengan 2 maka akan memunculkan pertanyaan apakah ingin keluar atau tidak
    elif menuss == "2":
        # di sini saya membuat pertanyaan apakah ingin keluar atau tidak
        print("Are you sure you want to exit? Y/N")
        # di sini saya membuat inputan untuk pertanyaan tersebut yang akan disimpan dalam variabel choice
        choice = input()
        # jika choice sama dengan y maka program akan berhenti
        if choice.lower() == "y":
            break
        # selain itu jika choice sama dengan n maka program akan kembali ke awal
        elif choice.lower() == "n":
            continue
