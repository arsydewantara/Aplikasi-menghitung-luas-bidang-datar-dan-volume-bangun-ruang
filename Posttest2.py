def menu():
    print("Menu Utama")
    print(" ")
    print("Aplikasi Menghitung Luas Bidang Datar dan Volume Bangun Ruang")
    print(" ")
    print("Pilih 1 untuk Mencari Luas Bidang Datar")
    print("Pilih 2 untuk Mencari Volume Bangun Ruang")
    print(" ")
menu()

def Bidang_Datar():
    print(" ")
    print("Daftar Bidang Datar Yang Bisa Kamu Cari Luasnya")
    print("\n1.Persegi Panjang \n2.Segitiga \n3.Persegi \n4.Lingkaran \n5.Trapesium")

def Bangun_Ruang():
    print(" ")
    print("Daftar Bangun Ruang Yang Bisa Kamu Cari Volumenya")
    print("\n1.Balok \n2.Tabung \n3.Kubus")

def Keluar():
    print("Apakah Kamu Ingin Keluar Dari Program ?")
    print("Ketik Ya jika ingin Keluar")
    print("Ketik Tidak jika ingin Kembali Ke Menu")
    Keluar = input("Ya/Tidak = ")
    if Keluar == "Ya":
        exit()
    elif Keluar == "ya":
        exit()
    elif Keluar == "Tidak":
        menu()
    elif Keluar == "tidak":
        menu()


def luaspersegipanjang(p,l):
    print(" ")
    print("Mencari Luas Persegi Panjang")
    p=int(input("Masukkan Sisi Panjangnya: "))
    l=int(input("Masukkan Sisi Lebarnya: "))
    luas=(p*l)
    print("%d X %d = %d"%(p,l,luas))
    print("Luas Persegi Panjang Berdasarkan Panjang dan lebarnya adalah %s cm" %luas)

def luassegitiga(a,t):
    print(" ")
    print("Mencari Luas Segitiga")
    a=float(input("Masukkan Panjang alasnya: "))
    t=float(input("Masukkan Tingginya: "))
    luas=(a*t)/2
    print("%d X %d /2 = %d"%(a,t,luas))
    print("Luas Segitiga Berdasarkan Alas Dan Tinggi yang sudah di input adalah %s cm" %luas)

def luaspersegi(s):
    print("Mencari Luas Persegi")
    s=float(input("Masukkan panjang Sisi: "))
    luas=(s*s)
    print("%d X %d = %d"%(s,s,luas))
    print("Luas Persegi Berdasarkan Sisi yang sudah di input adalah %s cm" %luas)

def luaslingkaran(r):
    print("Mencari Luas Lingkaran")
    phi=3.14
    r=float(input("Masukkan Panjang jari jari: "))
    luas=(phi*(r*r))
    print("%d X (%d X %d)=%d"%(phi,r,r,luas))
    print("Luas Lingkaran Berdasarkan jari jari yang sudah di input adalah %s cm" %luas)

def luastrapesium(a,b,t):
    print("Mencari Luas Trapesium")
    a=float(input("Masukkan Panjang Sisi Atas Bangun Trapesium: "))
    b=float(input("Masukkan Panjang Sisi Bawah Bangun Trapesium: "))
    t=float(input("Masukkan Tinggi Bangun Trapesium: "))
    luas=(((a+b)/2)*t)
    print("((%d + %d)/2) X %d=%d"%(a,b,t,luas))
    print("Luas Bangun Trapesium Berdasarkan Panjang Sisi Atas Bawah Serta Tinggi yang sudah diinput adalah %s cm" %luas)

def volumebalok(p,l,t):
    print("Mencari Volume Balok")
    p=float(input("Masukkan Panjang Balok: "))
    l=float(input("Masukkan Lebar Balok: "))
    t=float(input("Masukkan Tinggi Balok: "))
    volume=(p*l*t)
    print("%d X %d X %d=%d"%(p,l,t,volume))
    print("Volume Bangun Ruang Balok Berdasarkan Panjang, Lebar, dan Tinggi yang sudah di input adalah %s cm^3" %volume)

def volumetabung(r,t):
    print("Mencari Volume Tabung")
    phi=3.14
    r=float(input("Masukkan Jari jari Tabung: "))
    t=float(input("Masukkan Tinggi Tabung: "))
    volume=(phi*(r*r)*t)
    print("(%d X(%d X %d)X %d=%d"%(phi,r,r,t,volume))
    print("Volume Bangun Ruang Tabung Berdasarkan Jari jari dan Tinggi yang sudah di input adalah %s cm^3" %volume)

def volumekubus(s):
    print("Mencari Volume Kubus")
    s=float(input("Masukkan Panjang Sisi Kubus: "))
    volume=(s*s*s)
    print("%d X %d X %d=%d"%(s,s,s,volume))
    print("Volume Bangun Ruang Kubus Berdasarkan Sisi yang sudah di input adalah %s cm^3" %volume)

while 1:
    pilih=input("Masukkan Jenis Bangun yang ingin kamu cari Luas atau Volumenya: ")
    if pilih == "1":
        Bidang_Datar()
        print("\n")
        print("Pilih Bangun Datar yang ingin kamu cari luasnya")
        print("Masukkan angka 1 atau 5 untuk memilih Bangun Datar")
        print(" ")
        pilih = input("Bangun Datar Yang Dipilih: ")
        if pilih == "1":
            print(" ")
            luaspersegipanjang('p','l')
            print("\n")
            Keluar()
        elif pilih == "2":
            print(" ")
            luassegitiga('a','t')
            print("\n")
            Keluar()
        elif pilih == "3":
            print(" ")
            luaspersegi('s')
            print("\n")
            Keluar()
        elif pilih == "4":
            print(" ")
            luaslingkaran('r')
            print("\n")
            Keluar()
        elif pilih == "5":
            print(" ")
            luastrapesium('a','b','t')
            print("\n")
            Keluar()

    elif pilih == "2":
        Bangun_Ruang()
        print("\n")
        print("Pilih Bangun Ruang yang ingin kamu cari luasnya")
        print("Masukkan Angka 1 sampai 3 untuk memilih Bangun Ruang")
        print(" ")
        pilih = input("Bangun Ruang yang Dipilih: ")
        if pilih == "1":
            print(" ")
            volumebalok('p','l','t')
            print("\n")
            Keluar()
        elif pilih == "2":
            print(" ")
            volumetabung('r','t')
            print("\n")
            Keluar()
        elif pilih == "3":
            print(" ")
            volumekubus('s')
            print("\n")
            Keluar()

    else:
        print(" ")
        print("Maaf, Pilihan anda tidak tersedia")
        print("Ingin Mencoba lagi [Ya/Tidak] ?")
        coba = input()
        if coba == "Ya":
            menu()
        elif coba == "ya":
            menu()
        elif coba == "Tidak":
            Keluar()
        elif coba == "tidak":
            Keluar()


