print ("=======================")
print ("program penghitung luas bangun datar")
print(''')
Pilih salah satu bangun datar:
1 = Luas Persegi
2 = Luas Lingkaran
3 = Luas Segitiga
''')

pilihan = input("Masukkan pilihan")
match pilihan:
   case 1:
       sisi = int(input("Masukan sisi"))
       luas = sisi * sisi
       print("Luas Persegi dengan sisi", sisi ,"adalah: ", luas)
       case 2:
           jari = int("Masukkan jari-jari: ")
           luas = 3.14 * jari ** 2
           print("Luas lingkaran dengan jari-jari",jari,"adalah: ", luas )
        case 3:
            alas = int(input("Masukkan alas"))
            tinggi = int(input("Masukkan tinggi"))
            luas = 1/2 * alas * tinggi
            print("Luas segitiga dengan alas", alas, " dan tinggi", tinggi, "adalah: ")
        case_:
            print("Pilihan salah.")