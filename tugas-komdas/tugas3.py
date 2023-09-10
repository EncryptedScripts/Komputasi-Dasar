import math
# di sini saya mengimport library math untuk menghitung akar kuadrat
import random
# di sini saya mengimport library random untuk mengacak angka

# pada fungsi menu ini saya membuat menu untuk memilih fungsi kuadrat atau swap 2 index pertama dari 2 array/list
# pilihan ke 2 dan ke 3 hanya tambahan saja
def menu():
    print(f"====================================")
    print(f"1) fungsi kuadrat")
    print(f"2) swap 2 index pertama dari 2 array/list")
    print(f"3) exit")

    # variabel x ini nanti akan diisi dengan inputan user
    x = int(input("Select one: "))
    
    # di sini akan mengembalikan nilai x
    return x

# pada fungsi "fungsi" ini saya membuat fungsi kuadrat yang nanti akan menghasilkan grafik dari fungsi kuadrat tersebut dan juga akan menghasilkan nilai x1 dan x2
def fungsi():
    # hanyalah sebuah border
    print("====================================")
    # saya menggunakan try dan except untuk menangkap error jika user menginputkan selain integer
    try:
        # di sini saya membuat inputan untuk nilai a, b, dan c untuk mengisi fungsi kuadrat ax^2 + bx + c
        print("format: ", "ax^2 + bx + c")
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        # jika user menginputkan nilai a, b, dan c yang kurang dari atau sama dengan 0 maka akan menghasilkan error
        # yang nanti akan ditangkap oleh except dan mengembalikan pada fungsi "fungsi"
        if (a <= 0 and b <= 0 and c <= 0):
            raise ValueError
    except ValueError:
        return fungsi()

    print("====================================")
    # di sini saya membuat variabel Determinan yang diisi dengan rumus b^2 - 4ac yaitu rumus untuk mencari determinan
    Determinan = (b**2) - (4*a*c)
    # di sini saya membuat print untuk menampilkan nilai determinan
    print("Determinan dari fungsi tersebut adalah: ", Determinan)
    # jika nilai determinan lebih dari 0 maka akan menghasilkan x1 dan x2
    if (Determinan > 0):
        # x1 dan x2 di sini menggunakan rumus (-b + sqrt(Determinan)) / 2a dan (-b - sqrt(Determinan)) / 2a
        # fungsi sqrt sendiri setelah saya baca baca merupakan fungsi dari library math untuk menghitung akar
        x1 = (-b + math.sqrt(Determinan)) / (2*a)
        x2 = (-b - math.sqrt(Determinan)) / (2*a)
        # di sini saya membuat variabel x1_round dan x2_round yang diisi dengan fungsi round untuk membulatkan nilai x1 dan x2 jadi jika nilai yang dihasilkan adalah 1.5 maka akan dibulatkan menjadi 2
        x1_round = round(x1)
        x2_round = round(x2)
        # di sini saya membuat print untuk menampilkan nilai x1 dan x2 yang sudah dibulatkan
        print("x1 = ", round(x1_round))
        print("x2 = ", round(x2_round))
        print("====================================")
        # di sini saya membuat list kosong untuk menampung nilai x1_round dan x2_round
        list1 = []
        list2 = []
        # di sini saya membuat list1 yang diisi dengan range dari x1_round sampai 11, 11 di sini bukan lah sampai index ke 11 melainkan sampai nilai pada index terakhir mencapai 10
        list1 = list(range(x1_round, 11))
        list2 = list(range(x2_round, 11))
        # di sini saya membuat print untuk menampilkan list1 dan list2
        print ("list1: ", list1)
        print ("list2: ", list2)
        print("====================================")
        # pada bagian ini saya membuat grafik dari fungsi kuadrat tersebut
        # dengan algoritma pada awal akan print x1 dan y lalu akan print nilai dari x1 dan akan print * sebanyak nilai dari x1
        print(f"x1\t| ")
        print(f"y\t| ")
        # untuk lebih jelasnya pada bagian ini saya melakukan pengulangan sebanyak nilai dari list1 index ke 0 sampai nilai pada index terakhirnya adalah 10, saya menggunakan angka 11 karena jika saya menggunakan angka 10 maka nilai pada index terakhirnya adalah 9
        for i in range(list1[0], 11):
            # pada bagian ini saya membuat print yang akan dilakukan selama loop berlangsung yang akan menghasilkan nilai i untuk membuat list ke bawah dan akan menghasilkan * sebanyak nilai dari i - list1[0]
            print(f"{i}\t|{' ' * list1[i - list1[0]]}*")
        print("====================================")
        # kurang lebih saya menggunakan algoritma yang sama untuk menampilkan grafik dari x2
        print(f"x2\t| ")
        print(f"y\t| ")
        for i in range(list2[0], 11):
            print(f"{i}\t|{' ' * list2[i - list2[0]]}*")
    # selain itu jika hasil dari determinan adalah 0 maka akan menghasilkan x1 dan x2 yang sama
    elif (Determinan == 0):
        # x1 di sini menggunakan rumus yang sama dan pada x2 nilai nya sama dengan x1
        x1 = (-b + math.sqrt(Determinan)) / (2*a)
        x2 = x1

        # di sini saya melakukan pembulatan lagi seperti yang sudah saya jelaskan sebelumnya
        x1_round = round(x1)
        x2_round = round(x2)
        print("x1 = ", round(x1_round))
        print("x2 = ", round(x2_round))
        print("====================================")
        list1 = []
        list2 = []
        
        # pada algoritma pembuatan grafik pada kondisi ini saya menggunakan kurang lebih algoritma yang sama pada algoritma grafik di atas
        list1 = list(range(x1_round, 11))
        list2 = list(range(x2_round, 11))
        print ("list1: ", list1)
        print ("list2: ", list2)
        print("====================================")
        print(f"x1\t| ")
        print(f"y\t| ")
        for i in range(list1[0], 11):
            print(f"{i}\t|{' ' * list1[i - list1[0]]}*")
        print("====================================")
        print(f"x2\t| ")
        print(f"y\t| ")
        for i in range(list2[0], 11):
            print(f"{i}\t|{' ' * list2[i - list2[0]]}*")
        
    # selain itu jika hasil dari determinan adalah kurang dari 0 maka akan menghasilkan akar tidak real maupun imajiner
    else:
        print(f'akar tidak real maupun imajiner')

# pada fungsi swap (ini hanyalah tambahan dari saya) saya membuat fungsi untuk menukar 2 index pertama dari 2 array/list
def swap():
    print("====================================")
    # pada x1 dan y2 saya membuat list kosong untuk menampung nilai dari inputan user
    x1 = []
    y2 = []

    # lagi lagi saya menggunakan error handling try dan except agar jika inputan dari user selain integer maka akan menghasilkan error dan kembali ke fungsi swap. Tujuannya agar tidak crash programnya
    try:
        x = int(input("array length x: "))
        y = int(input("array length y: "))
        if (x < 0 and y < 0):
            raise ValueError
    except ValueError:
        print("Please enter a positive integer")
        return swap()

    # pada bagian ini saya membuat perulangan untuk mengisi list x1 dan y2 dengan angka random dari 0 sampai 100 sebanyak nilai dari x dan y yang diinputkan
    for i in range(x):
        x1.append(random.randint(0, 100))
    for i in range(y):
        y2.append(random.randint(0, 100))

    # di sini saya membuat print hasil dari list x1 dan y2
    print("x1: ", x1)
    print("y2: ", y2)
    print("====================================")
    # pada bagian ini saya membuat swap dari 2 index pertama dari list x1 dan y2
    y2[0], x1[0] = x1[0], y2[0]
    # yang akan menghasilkan hasil swap atau penukaran index pertama dari list x1 dan y2 yang nanti akan saya print
    print("swap result x1: ", x1)
    print("swap result y2: ", y2)
    print("====================================")
    





# pada bagian ini saya menggunakan while loop dengan value true agar programnya dapat berjalan terus menerus
while (True):
    # di sini saya membuat variabel pilihan yang diisi dengan fungsi menu agar lebih mudah untuk dipanggil
    pilihan = menu()
    # jika pilihan adalah 1 maka akan memanggil fungsi "fungsi"
    if (pilihan == 1):
        fungsi()
    # selain itu jika pilihan adalah 2 maka akan memanggil fungsi "swap"
    elif (pilihan == 2):
        swap()
    # selain itu jika pilihan adalah 3 maka akan menghentikan program
    elif (pilihan == 3):
        break
    # selain dari kondisi kondisi di atas maka akan menghasilkan print "wrong input" dan akan kembali ke fungsi menu
    else:
        print("wrong input")
        continue