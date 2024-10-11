bulan = ''
while (bulan != -1):
    print("Masukan -1 jika ingin menghentikan program")
    bulan = int(input("Masukan bulan (1-12): "))
    
    if (bulan == 1):
        hari = 31
        print("Jumlah hari = ", hari)
    elif(bulan == 2):
        tahun = int(input("Masukan tahun (e.g., 2021): "))
        if((tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)):
            hari = 29
        else:
            hari = 28
        print("Jumlah hari = ", hari)
    elif(bulan == 3):
        hari = 31
        print("Jumlah hari = ", hari)
    elif(bulan == 4):
        hari = 30
        print("Jumlah hari = ", hari)
    elif(bulan == 5):
        hari = 31
        print("Jumlah hari = ", hari)
    elif(bulan == 6):
        hari = 30
        print("Jumlah hari = ", hari)
    elif(bulan == 7):
        hari = 31
        print("Jumlah hari = ", hari)
    elif(bulan == 8):
        hari = 31
        print("Jumlah hari = ", hari)
    elif(bulan == 9):
        hari = 30
        print("Jumlah hari = ", hari)
    elif(bulan == 10):
        hari = 31
        print("Jumlah hari = ", hari)
    elif(bulan == 11):
        hari = 30
        print("Jumlah hari = ", hari)
    elif(bulan == 12):
        hari = 31
        print("Jumlah hari = ", hari)
    else:
        if bulan != -1:
            print("Invalid data")
