n = int(input("Masukkan nilai: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end="")
    print()  