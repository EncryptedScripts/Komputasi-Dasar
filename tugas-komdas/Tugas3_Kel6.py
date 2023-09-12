#########################################
#
# Tugas 3 Komputasi Dasar
#--------------------------
# Kelompok : 6 MAT59
# Tim programmer:
# 1. M. Naufal Afif (G5401221099)
# 2. Andyana Lilmuttaqina Mafaza (G6401211002)
# 3. Bagus Muliasa Insani (G5401221047) 
# 4. Nadhifa Zahra Ghaisani (G5401221057)
# 5. Nadhira Maulida Hayani (G5401221004) 
# 6. Septiana Isna Dian Noor (G5401221014) 
#
# Tanggal upload : 12 September 2023

import matplotlib.pyplot as plt
import numpy as np
# di sini saya meng import 2 library, yaitu matplotlib.pyplot dan numpy
# matplotlib.pyplot digunakan untuk membuat plot
# numpy digunakan untuk membuat array yang akan digunakan untuk membuat plot dan dapat digunakan untuk melakukan operasi matematika

# pada fungsi 0 saya menggunakan np.zeros_like(x) untuk membuat array yang berisi 0 dengan panjang yang sama dengan array x
def f0(x):
    return np.zeros_like(x)

# pada fungsi 1 saya menggunakan x untuk membuat array yang berisi nilai x
def f1(x):
    return x

# pada fungsi 2 saya menggunakan (x - 2) ** 2 untuk membuat array yang berisi nilai (x - 2) ** 2 yaitu (x - 2) pangkat 2
def f2(x):
    return (x - 2) ** 2

# pada fungsi 3 saya menggunakan 10 * np.sin(x) untuk membuat array yang berisi nilai 10 * sin(x)
def f3(x):
    return 10 * np.sin(x)

# pada fungsi 4 saya menggunakan np.exp(x) untuk membuat array yang berisi nilai e ** x yaitu e pangkat x
def f4(x):
    return np.exp(x)

# pada fungsi plot saya menggunakan np.linspace(a, b, c) untuk membuat array yang berisi nilai dari a sampai b sebanyak c
def plot(a, b, c):
    x = np.linspace(a, b, c)

    # pada bagian ini saya menggunakan plt.plot(x, f(x)) untuk membuat plot dari fungsi f(x) dengan nilai x
    plt.plot(x, f0(x), label='f0(x) = 0')
    plt.plot(x, f1(x), label='f1(x) = x')
    plt.plot(x, f2(x), label='f2(x) = (x - 2)^2')
    plt.plot(x, f3(x), label='f3(x) = 10sin(x)')
    plt.plot(x, f4(x), label='f4(x) = e^x')
    
    # pada bagian ini saya menggunakan plt.fill_between(x, f(x), f(x)) untuk membuat area antara fungsi f(x) dan f(x) dengan nilai x dan menggunakan where=(f(x) <= f(x)) untuk mengisi area yang berada di bawah fungsi f(x)
    plt.fill_between(x, f0(x), f1(x), where=(f0(x) <= f1(x)), interpolate=True, alpha=0.5, label='Area antara f0(x) dan f1(x)')
    plt.fill_between(x, f2(x), f1(x), where=(f2(x) <= f1(x)), interpolate=True, alpha=0.5, label='Area antara f2(x) dan f1(x)')
    plt.fill_between(x, f3(x), f1(x), where=(f3(x) <= f1(x)), interpolate=True, alpha=0.5, label='Area antara f3(x) dan f1(x)')
    plt.fill_between(x, f4(x), f1(x), where=(f4(x) <= f1(x)), interpolate=True, alpha=0.5, label='Area antara f4(x) dan f1(x)')

    # pada bagian ini hanya untuk mengatur tampilan plot seperti judul, label, grid, dan lain-lain
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Primitive Function Plot')
    plt.grid(True)
    plt.show()

# pada bagian ini saya menggunakan try-except untuk menangani error jika input yang dimasukkan bukan berupa angka
try:
    a = int(input('Masukkan input 1: '))
    b = int(input('Masukkan input 2: '))
    c = int(input('Masukkan input 3: '))
    
    if (a != int and b != int and c != int):
        raise ValueError
except ValueError:
    print('Input harus berupa angka!')

# jika tidak ada error input maka akan menjalankan fungsi plot
plot(a, b, c)
    





