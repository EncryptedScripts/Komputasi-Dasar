# di sini saya membuat fungsi masing masing agar mempermudah untuk dipanggil saat melakukan eksekusi

# pada fungsi main_menu saya membuat menu yang akan ditampilkan saat program dijalankan
# sebenarnya ini di luar tugas jadi hanya tambahan dari saya saja, saya mengkombinasi soal yang ada di PPT dan tugas ini menjadi list menu
def main_menu():
    Logo = ''' ________  ___    ___ _________  ___  ___  ________  ________   _____ ______   _______   ________   ___  ___     
|\   __  \|\  \  /  /|\___   ___\\  \|\  \|\   __  \|\   ___  \|\   _ \  _   \|\  ___ \ |\   ___  \|\  \|\  \    
\ \  \|\  \ \  \/  / ||___ \  \_\ \  \\\  \ \  \|\  \ \  \\ \  \ \  \\\__\ \  \ \   __/|\ \  \\ \  \ \  \\\  \   
 \ \   ____\ \    / /     \ \  \ \ \   __  \ \  \\\  \ \  \\ \  \ \  \\|__| \  \ \  \_|/_\ \  \\ \  \ \  \\\  \  
  \ \  \___|\/  /  /       \ \  \ \ \  \ \  \ \  \\\  \ \  \\ \  \ \  \    \ \  \ \  \_|\ \ \  \\ \  \ \  \\\  \ 
   \ \__\ __/  / /          \ \__\ \ \__\ \__\ \_______\ \__\\ \__\ \__\    \ \__\ \_______\ \__\\ \__\ \_______\
    \|__||\___/ /            \|__|  \|__|\|__|\|_______|\|__| \|__|\|__|     \|__|\|_______|\|__| \|__|\|_______|
         \|___|/                                                                                                 
                                                                                                                 
                                                                                                                  '''

    print(Logo)
    print("Welcome to the Selection Menu!")
    print("1. Comparison between Annie and Ellie's Age")
    print("2. Summary of total money you have")
    print("3. triangle area")
    print("4. Find the minimum in the array")
    print("5. Enter 4 name")
    print("6. Exit")
    # saya menggunakan input agar user dapat memilih menu yang diinginkan
    choice = input("Enter your choice: ")
    # saya menggunakan return agar dapat mengembalikan nilai dari fungsi main_menu
    return choice


# pada fungsi Comparison saya membuat perbandingan umur antara Annie dan Ellie
def Comparison(Annie, Ellie):
    # saya menggunakan if, elif, else agar dapat membandingkan umur antara Annie dan Ellie

    if Annie > Ellie:
        # Jika Annie lebih tua dari Ellie maka akan menampilkan "Annie is older than Ellie"
        print("Annie is older than Ellie")
    elif Annie < Ellie:
        # Jika Annie lebih muda dari Ellie maka akan menampilkan "Annie is younger than Ellie"
        print("Annie is younger than Ellie")
    else:
        # Jika Annie dan Ellie memiliki umur yang sama maka akan menampilkan "Annie & Ellie's age is the same"
        print("Annie & Ellie's age is the same")


# pada fungsi SummaryOfMoney saya membuat perhitungan jumlah uang yang dimiliki oleh user


def SummaryOfMoney(money1, money2, money3):
    # pada fungsi ini dibutuhkan 3 parameter yaitu money1, money2, money3 yang masing masing berupa integer
    # result adalah variabel yang berfungsi untuk menampung hasil dari perhitungan jumlah uang yang dimiliki oleh user
    Result = int(money1) + int(money2) + int(money3)
    # saya menggunakan print untuk menampilkan hasil dari perhitungan jumlah uang yang dimiliki oleh user
    print("The total of money you have is: " + str(Result))


# pada fungsi triangle saya membuat perhitungan luas segitiga
def triangle(width, length):
    print("Select the type")
    print("1. centimeter")
    print("2. milimeter")
    print("3. meter")
# saya menggunakan input agar user dapat memilih menu yang diinginkan
# pada menu ini user dapat memilih centimeter, milimeter, atau meter
    choice = int(input("Enter your choice: "))

# saya menggunakan if, elif, else agar dapat memilih menu yang diinginkan
# jika yang dipilih adalah centimeter maka akan menampilkan hasil perhitungan luas segitiga dalam satuan centimeter
    if choice == 1:
        # di sinilah saya membuat perhitungan luas segitiga
        AlasKaliTinggi = int(width) * int(length)
        # variabel result berfungsi untuk menampung hasil dari perhitungan luas segitiga
        Result = AlasKaliTinggi / 2
        # saya menggunakan print untuk menampilkan hasil dari perhitungan luas segitiga
        print("The result of area of the triangle is: " + str(Result) + " cm^2")
        # saya menggunakan for loop agar dapat menampilkan bentuk segitiga
        # n adalah variabel yang berfungsi untuk menampung nilai 10
        # pada for loop ini saya membuat bentuk segitiga dengan menggunakan bintang (*) dan spasi ( ) agar dapat menampilkan bentuk segitiga

        n = 10
        for i in range(1, n+1):
            print(' ' * n, end='')
            print('* '*(i))
            n -= 1
    elif choice == 2:
        # pada pilihan ke 2 sama juga hanya saja hasil dari perhitungan luas segitiga akan ditampilkan dalam satuan milimeter
        AlasKaliTinggi = int(width) * int(length)
        Result = AlasKaliTinggi / 2
        print("The result of area of the triangle is: " + str(Result) + " mm^2")
        n = 10
        for i in range(1, n+1):
            print(' ' * n, end='')
            print('* '*(i))

            n -= 1
    elif choice == 3:
        # pada pilihan ke 3 sama juga hanya saja hasil dari perhitungan luas segitiga akan ditampilkan dalam satuan meter
        AlasKaliTinggi = int(width) * int(length)
        Result = AlasKaliTinggi / 2
        print("The result of area of the triangle is: " + str(Result) + " m^2")
        n = 10
        for i in range(1, n+1):
            print(' ' * n, end='')
            print('* '*(i))
            n -= 1


def Arrays():
    # pada fungsi Arrays saya membuat perhitungan nilai terkecil dari array yang diinput oleh user sama seperti yang ada dalam ppt namun saya customize lagi
    # saya menggunakan try, except dan raise agar dapat menangani error yang terjadi saat user menginputkan nilai yang tidak sesuai
    # intinya try, except dan raise berfungsi untuk error handling untuk mencegah crash saat ada kesalahan input dari user
    try:
        num_elements = int(
            # saya menggunakan input agar user dapat menginputkan nilai yang diinginkan
            input("Enter the number of elements in the array: "))
        if num_elements < 0:
            # jika user menginputkan nilai negatif maka akan menampilkan "The number of elements cannot be negative. Please try again."
            raise ValueError
    except ValueError:
        print("The number of elements cannot be negative or a string. Please try again.")
        return Arrays()
    # intinya buat error handling lah biar programnya tidak crash saat ada kesalahan input dari user

    # saya menggunakan for loop agar user dapat menginputkan nilai yang diinginkan sesuai dengan jumlah elemen yang diinputkan
    array = []
    for i in range(num_elements):
        try:
            element = int(input(f"Enter element {i+1}: "))
            array.append(element)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return Arrays()

    # saya menggunakan min untuk menampilkan nilai terkecil dari array yang diinput oleh user
    min_value = min(array)
    print(f"The minimum value in the array is: {min_value}")

# pada fungsi Names saya membuat perhitungan jumlah karakter dari nama yang diinput oleh user


def Names(name1, name2, name3, name4):
    names = [name1, name2, name3, name4]
    nameApip = "Encrypted"
    NIM = "16520299"
    max_length = max(len(name) for name in names)
    border = "----------------------------------"

    # saya menggunakan for loop agar dapat menampilkan jumlah karakter dari nama yang diinput oleh user
    for name in names:
        print(f"{name} has {len(name)} characters.")
        print(border)
    # saya menggunakan if, else agar dapat menampilkan nama yang diinput oleh user
    # pada perkondisian pertama jika jumlah karakter dari nama yang diinput oleh user lebih dari 30 maka akan menampilkan "The limit of each character for each name input is 30 characters"
    if any(len(name) > 30 for name in names):
        print("The limit of each character for each name input is 30 characters")
        print(border)
        return Names(name1, name2, name3, name4)
    else:
        # pada perkondisian kedua jika jumlah karakter dari nama yang diinput oleh user kurang dari 30 maka akan menampilkan nama yang diinput oleh user
        print(f"{border}")
        print("||    NIM     ||    Name         ||")
        print(f"{border}")
        print("||" + NIM + " ||" + nameApip + " " *
              (max_length - len(name1)) + "||")
        print(f"{border}")
        print("||  5 Number     ||    Name      ||")
        print(f"{border}")
        print("||   " + "1.     ||" + name1 + " " *
              (max_length - len(name1)) + "||")
        print("||   " + "2.     ||" + name2 + " " *
              (max_length - len(name2)) + "||")
        print("||   " + "3.     ||" + name3 + " " *
              (max_length - len(name3)) + "||")
        print("||   " + "4.     ||" + name4 + " " *
              (max_length - len(name4)) + "||")
        print(border)
        # pada bagian "||   " + "1.     ||" + name1 + " " * (max_length - len(name1)) + "||") saya menggunakan max_length - len(name1) agar dapat menampilkan nama yang diinput oleh user sesuai dengan jumlah karakter yang diinput oleh user dan membuat border agar tampilan lebih rapih


# saya menggunakan while True agar program dapat berjalan terus menerus sampai user memilih menu exit
while True:
    selected_option = main_menu()
    # di sini saya tidak menggunakan if, elif, dan else melainkan menggunakan match dan case, di sini sama seperti switch case pada bahasa pemrograman lain
    # match dan case menurut saya lebih optimal dan lebih mudah dibaca daripada if, elif, dan else karena match dan case hanya membandingkan nilai yang diinput oleh user dengan nilai yang ada di case
    match selected_option:
        case "1":
            print("Enter Annie's Age: ")
            AnnAge = input()
            print("Enter Ellie's Age: ")
            EllAge = input()
            Comparison(AnnAge, EllAge)
            print("----------------------------------")

        case "2":
            print("Enter the amount of money1: ")
            Monn1 = input()
            print("Enter the ammount of money2: ")
            Monn2 = input()
            print("Enter the ammount of money3: ")
            Monn3 = input()
            print("----------------------------------")

            SummaryOfMoney(Monn1, Monn2, Monn3)

        case "3":
            print("Input the width: ")
            width1 = input()
            print("Input the length: ")
            length1 = input()
            triangle(width1, length1)
            print("----------------------------------")
        case "4":
            Arrays()
            print("----------------------------------")
        case "5":
            print("Enter a name for name1: ")
            names1 = input(str())
            print("----------------------------------")
            print("Enter a name for name2: ")
            names2 = input(str())
            print("----------------------------------")
            print("Enter a name for name3: ")
            names3 = input(str())
            print("----------------------------------")
            print("Enter a name for name4: ")
            names4 = input(str())
            print("----------------------------------")
            Names(names1, names2, names3, names4)
            print("----------------------------------")
        case "6":
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please select a valid option.")
            print("----------------------------------")
