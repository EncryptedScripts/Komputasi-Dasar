import math

#########
# f0(x)


def f0(x):
    'f(x) = 0'
    return 0

#########
# f1(x)


def f1(x):
    'f(x) = x'
    return x

#########
# f2(x)


def f2(x):
    'f(x) = (x-2)^2'
    return (x-2)**2

#########
# f3(x)


def f3(x):
    'f(x) = 10*sin(x)'
    return 10*math.sin(x)

#########
# f4(x)


def f4(x):
    'f(x) = exp(x)'
    return math.exp(x)

###################
# Plot function
# ---------------


def myPlot(f, xmin, xmax):
    'Plot function f(x) for x in [xmin, xmax]'
    x_values = []
    y_values = []
    step = 0.1  # Step size for x-axis values
    x = xmin

    while x <= xmax:
        x_values.append(x)
        y_values.append(f(x))
        x += step

    # Print function help and range
    print(f"Help on function {f.__name__} in module __main__:")
    print(f"{f.__name__}(x)")
    print(f"    {f.__doc__}\n")
    print(f"[xmin, xmax] = [{xmin}, {xmax}]")
    print(f"[ymin, ymax] = [{min(y_values)}, {max(y_values)}]")

    # Plot the function
    for y in reversed(range(int(min(y_values)), int(max(y_values)) + 1)):
        line = ""
        for i in range(len(x_values)):
            if y <= int(y_values[i]) <= y + 1:
                line += "*"
            else:
                line += " "
        print(line)
    print("\n")
    # return minimum and maximum values of the function
    return [min(y_values), max(y_values)]
    # return [ymin, ymax]  # return minimum and maximum values of the function

####################################
# Plot area between two functions
# -----------------------------------


def myPlotArea(f1, f2, xmin, xmax):
    'Plot area between two functions f1(x) and f2(x) for x in [xmin, xmax]'
    #
    # tuliskan di sini langkah-langkah untuk menunaikan tugas tersebut
    #
    #
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

    # Print function help and range
    print(f"Help on function {f1.__name__} in module __main__:")
    print(f"{f1.__name__}(x)")
    print(f"    {f1.__doc__}\n")
    print(f"Help on function {f2.__name__} in module __main__:")
    print(f"{f2.__name__}(x)")
    print(f"    {f2.__doc__}\n")
    print(f"[xmin, xmax] = [{xmin}, {xmax}]")
    print(
        f"[ymin, ymax] = [{min(min(y1_values), min(y2_values))}, {max(max(y1_values), max(y2_values))}]")

    # Calculate the area between the two functions
    area = 0
    for i in range(len(x_values) - 1):
        dx = x_values[i + 1] - x_values[i]
        area += 0.5 * (y1_values[i] + y1_values[i + 1]) * \
            dx - 0.5 * (y2_values[i] + y2_values[i + 1]) * dx

    # Plot the area
    for y in reversed(range(int(min(min(y1_values), min(y2_values))), int(max(max(y1_values), max(y2_values))) + 1)):
        line = ""
        for i in range(len(x_values)):
            if y1_values[i] >= y >= y2_values[i] or y2_values[i] >= y >= y1_values[i]:
                line += "*"
            else:
                line += " "
        print(line)
    print("\n")

    # Print the calculated area
    print(f"Area between the two functions: {area}\n")
    return [min(min(y1_values), min(y2_values)), max(max(y1_values), max(y2_values))]
    # return [ymin, ymax]  # return minimum and maximum values of the functions


###########################
# Program utama
# ---------------
# fungsi-fungsi yang diplot dan daerah asal fungsi
flist = [f1, f2, f3, f4]
xmin = [0,  0, -math.pi, -1]
xmax = [1,  5, 2*math.pi, 3]

# plot fungsi-fungsi
print('============ PLOT FUNCTIONS ============')
for i in range(len(flist)):
    help(flist[i])
    myPlot(flist[i], xmin[i], xmax[i])

# plot area between two functions
print()
print('============ PLOT AREA BETWEEN TWO FUNCTIONS ============')
for i in range(len(flist)):
    if i == 0:
        help(f0)
        help(flist[i])
        myPlotArea(f0, flist[i], xmin[i], xmax[i])
    else:
        help(f1)
        help(flist[i])
        myPlotArea(f1, flist[i], xmin[i], xmax[i])
