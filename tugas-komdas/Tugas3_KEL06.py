import math

# Fungsi-fungsi yang diberikan
def f0(x):
    'f(x) = 0'
    return 0

def f1(x):
    'f(x) = x'
    return x

def f2(x):
    'f(x) = (x-2)^2'
    return (x-2)**2

def f3(x):
    'f(x) = 10*sin(x)'
    return 10*math.sin(x)

def f4(x):
    'f(x) = exp(x)'
    return math.exp(x)

# Fungsi untuk plotting
def plot_function(f, xmin, xmax):
    'Plot function f(x) for x in [xmin, xmax]'
    x_values = []
    y_values = []
    step = 0.1  # Step size for x-axis values
    x = xmin

    while x <= xmax:
        x_values.append(x)
        y_values.append(f(x))
        x += step

    # Mencetak informasi tentang fungsi yang diplot
    print(f"Help on function {f.__name__} in module __main__:")
    print(f"{f.__name__}(x)")
    print(f"    {f.__doc__}\n")
    print(f"[xmin, xmax] = [{xmin}, {xmax}]")
    print(f"[ymin, ymax] = [{min(y_values)}, {max(y_values)}]")

    # Mencetak grafik fungsi pada layar
    for y in reversed(range(int(min(y_values)), int(max(y_values)) + 1)):
        line = "".join("*" if y <= int(y_val) <= y + 1 else " " for y_val in y_values)
        print(line)
    print("\n")

def plot_area_between_functions(f1, f2, xmin, xmax):
    'Plot area between two functions f1(x) and f2(x) for x in [xmin, xmax]'
    x_values = []
    y1_values = []
    y2_values = []
    step = 0.1  # Step size for x-axis values
    x = xmin

    while x <= xmax:
        x_values.append(x)
        y1_values.append(f1(x))
        y2_values.append(f2(x))
        x += step

    # Mencetak informasi tentang dua fungsi yang akan diplot
    print(f"Help on function {f1.__name__} in module __main__:")
    print(f"{f1.__name__}(x)")
    print(f"    {f1.__doc__}\n")
    print(f"Help on function {f2.__name__} in module __main__:")
    print(f"{f2.__name__}(x)")
    print(f"    {f2.__doc__}\n")
    print(f"[xmin, xmax] = [{xmin}, {xmax}]")
    print(
        f"[ymin, ymax] = [{min(min(y1_values), min(y2_values))}, {max(max(y1_values), max(y2_values))}]")

    area = 0
    for i in range(len(x_values) - 1):
        dx = x_values[i + 1] - x_values[i]
        # Menghitung luas area di antara dua fungsi menggunakan metode trapesium
        area += 0.5 * (y1_values[i] + y1_values[i + 1]) * \
            dx - 0.5 * (y2_values[i] + y2_values[i + 1]) * dx

    # Mencetak grafik area di antara dua fungsi pada layar
    for y in reversed(range(int(min(min(y1_values), min(y2_values))), int(max(max(y1_values), max(y2_values))) + 1)):
        line = "".join(
            "*" if y1 >= y >= y2 or y2 >= y >= y1 else " " for y1, y2 in zip(y1_values, y2_values))
        print(line)
    print("\n")

    # Mencetak nilai area yang dihitung
    print(f"Area between the two functions: {area}\n")

# Program utama
flist = [f1, f2, f3, f4]
xmin = [0,  0, -math.pi, -1]
xmax = [1,  5, 2*math.pi, 3]

print('============ PLOT FUNCTIONS ============')
for i in range(len(flist)):
    plot_function(flist[i], xmin[i], xmax[i])

print()
print('============ PLOT AREA BETWEEN TWO FUNCTIONS ============')
for i in range(len(flist)):
    if i == 0:
        # Memplot area antara f0 dan f1
        plot_area_between_functions(f0, flist[i], xmin[i], xmax[i])
    else:
        # Memplot area antara f1, f2, f3, dan f4 dengan fungsinya masing-masing
        plot_area_between_functions(f1, flist[i], xmin[i], xmax[i])
