# Keishaf
#Program ini dibuat untuk memudahkan user menghitung resep roti secara dinamis
import os
import msvcrt

resep_roti_Tawar ={
        "Tepung Terigu"         : 1010,
        "Gula Pasir"            : 90,
        "Ragi"                  : 15,
        "Mentega"               : 90,
        "Air"                   : 550,
        "Garam"                 : 12,
        "Bread Improver"        :2
}

resep_donat ={      
        "Tepung Terigu (gram)": 250,
        "Gula Pasir (gram)": 30,
        "Ragi (gram)" : 4,
        "Mentega (gram)" : 30,
        "Air (ml)" : 50,
        "Garam (gram)" : 3,
        "Susu Bubuk (gram)" : 15,
        "Bread Improver (gram)" : 1,
        "Telur (butir)" : 1,
}

resep_basePizza ={      
        "Tepung Terigu (gram)": 2640,
        "Gula Pasir (gram)": 225,
        "Ragi (gram)" : 30,
        "Mentega (gram)" : 300,
        "Air (ml)" : 1560,
        "Garam (gram)" : 10,
        "Susu Bubuk (gram)" : 80,
        "Bread Improver (gram)" : 7.5,
}

resep_rotiBantal ={      
        "Tepung Terigu (gram)": 940,
        "Gula Pasir (gram)": 170,
        "Ragi (gram)" : 15,
        "Margarin (gram)" : 52,
        "Air (ml)" : 525,
        "Garam (gram)" : 9,
        "Susu Bubuk (gram)" : 57,
        "Bread Improver (gram)" : 3,
        "BOS / Mentega (gram)" : 60,
}

resep_bunsBurger = {
        "Tepung Terigu (gram)": 770,
        "Gula Pasir (gram)": 140,
        "Ragi (gram)" : 14,
        "Mentega (gram)" : 43,
        "Air (ml)" : 430,
        "Garam (gram)" : 7,
        "Susu Bubuk (gram)" : 46,
        "Bread Improver (gram)" : 2,
        "BOS (gram)" : 49,
}


 


os.system('cls')
teks = ("SiKaReRo")
teks2 = ("Sistem Kalkulasi Resep Roti")
teks1 ="by Keishaf Krisna A.P"
teks_tengah = teks.center(75)
teks1_tengah = teks1.center(74)
teks2_tengah = teks2.center(75)

while True:
    
        
    os.system('cls')
    print ("\033[33m" + teks_tengah + "\033[0m")
    print ("\033[32m" + teks2_tengah + "\033[0m")
    print ("\033[34m" + teks1_tengah + "\033[0m")

    print("Masukkan input :")
    print("1. Roti Tawar Bandung")
    print("2. Donat")
    print("3. Base Pizza")
    print("4. Roti Bantal")
    print("5. Roti Buns Burger")
    print("6. Selesai ")

    Pilihan_menu = str(input("Masukkan input : "))
    
    if Pilihan_menu == "1":
            os.system('cls')
            
            teksRoti = ("ROTI TAWAR BANDUNG")
            teksRoti_tengah = teksRoti.center(75)
            print (teksRoti_tengah)
            print(f"Berikut ini merupakan daftar resep Roti Tawar Bandung")
            print(f"Untuk 6 Roti dengan Graminasi 290 gram/loyang \n")
            for bahan, jumlah in resep_roti_Tawar.items():
                    print(f"{bahan:<20} = {jumlah:>5} gram ")
                
                
            while True:
                try:
                    roti = int(input(f"\nIngin buat berapa roti ?"))
                    break
                except ValueError:
                    print("Jawaban tidak valid, coba lagi")
                    
            koefisienRoti = float(roti / 6)
            print (f"     ")
            print(f"Untuk membuat Roti Tawar Bandung Sejumlah {roti}  :")    
            print(f"Jadi anda memerlukan bahan bahan sebanyak dibawah :")
            print("Tepung terigu    = ", round(resep_roti_Tawar["Tepung Terigu"]*koefisienRoti), "gram")
            print("Gula Pasir       = ", round(resep_roti_Tawar["Gula Pasir"]*koefisienRoti   ), "gram")
            print("Ragi             = ", round(resep_roti_Tawar["Ragi"]*koefisienRoti   ),       "gram")
            print("Mentega          = ", round(resep_roti_Tawar["Mentega"]*koefisienRoti),       "gram")
            print("Air              = ", round(resep_roti_Tawar["Air"]*koefisienRoti),           "ml")
            print("Garam            = ", round(resep_roti_Tawar["Garam"]*koefisienRoti),         "gram")
            print("Bread Improver   = ", round(resep_roti_Tawar["Bread Improver"]*koefisienRoti),"gram")
            print ("     ")
            input("Tekan Enter untuk kembali ke menu...")
   
   
    elif Pilihan_menu == "2":
            os.system('cls')
            graminasi = 20
            jumlahDonat = 23
            
            teksDonat = ("==========RESEP DONAT==========")
            teksDonat_tengah = teksDonat.center(75)
            print (teksDonat_tengah)

            print("Berikut ini merupakan daftar resep Donat")
            print(f"\nuntuk 23 Donut dengan graminasi {graminasi} gram per donut     \n")
            for bahan, jumlah in resep_donat.items():
                        print(f"{bahan:<20} = {jumlah:>5} ")
            
            print("     ")    
            while True:
                try:
                    banyakDonat = int(input(f"Ingin membuat berapa donut?"))
                    break
                except ValueError:
                    print("Jawaban tidak valid, coba lagi")

            print("     ")

            while True:
                try:
                    massaDonat = int(input(f"Berapa graminasi setiap donat? (gram)"))
                    break
                except ValueError:
                    print("Jawaban tidak valid, coba lagi")
           
            print("     ")             
            rumus_donat = graminasi*jumlahDonat
            koefisien_donat = float((banyakDonat*massaDonat)/rumus_donat)
                
            print(f"Jadi untuk membuat Donut Sejumlah {banyakDonat} dengan graminasi {massaDonat} gram per donat, bahan bahan yang dibutuhkan adalah :")
            print("Tepung Terigu     =", round(resep_donat["Tepung Terigu (gram)"]*koefisien_donat), "gram")
            print("Gula Pasir        =", round(resep_donat["Gula Pasir (gram)"]*koefisien_donat),    "gram")
            print("Ragi              =", round(resep_donat["Ragi (gram)"]*koefisien_donat),          "gram")
            print("Mentega           =", round(resep_donat["Mentega (gram)"]*koefisien_donat),       "gram")
            print("Air               =", round(resep_donat["Air (ml)"]*koefisien_donat),             "gram")
            print("Garam             =", round(resep_donat["Garam (gram)"]*koefisien_donat),         "gram")
            print("Susu Bubuk        =", round(resep_donat["Susu Bubuk (gram)"]*koefisien_donat),    "gram")
            print("Bread Improver    =", round(resep_donat["Bread Improver (gram)"]*koefisien_donat),"gram")
            print("Telur             =", round(resep_donat["Telur (butir)"]*koefisien_donat),        "Butir")
            print ("     ")
            input("Tekan Enter untuk kembali ke menu...")

    elif Pilihan_menu == "3":
            os.system('cls')
            
            teksRoti = ("ROTI BASE PIZZA")
            teksRoti_tengah = teksRoti.center(75)
            print (teksRoti_tengah)

            graminasi = 158
            jumlahBase = 30
              
            print(f"Berikut ini merupakan daftar resep Roti Base Pizza")
            print(f"Untuk 30 Roti dengan Graminasi 158 gram/loyang \n")
            for bahan, jumlah in resep_basePizza.items():
                    print(f"{bahan:<20} = {jumlah:>5} gram ")

            print("     ")    
            while True:
                try:
                    banyakBase_pizza = int(input(f"Ingin membuat berapa Base Pizza?"))
                    break
                except ValueError:
                    print("Jawaban tidak valid, coba lagi")

            print("     ")

            while True:
                try:
                    massaBase_pizza = int(input(f"Berapa graminasi setiap Base Pizza? (gram)"))
                    break
                except ValueError:
                    print("Jawaban tidak valid, coba lagi")        

            print("     ")
            
            
            rumus_basePizza = graminasi*jumlahBase
            koefisien_basePizza = float((banyakBase_pizza*massaBase_pizza)/rumus_basePizza)

            print(f"Jadi untuk membuat base Pizza sejumlah {banyakBase_pizza} dengan graminasi {massaBase_pizza} gram per Base Pizza, bahan bahan yang dibutuhkan adalah :")
            print("Tepung Terigu     =", round(resep_basePizza["Tepung Terigu (gram)"]*koefisien_basePizza),    "gram")
            print("Gula Pasir        =", round(resep_basePizza["Gula Pasir (gram)"]*koefisien_basePizza),       "gram")
            print("Ragi              =", round(resep_basePizza["Ragi (gram)"]*koefisien_basePizza),             "gram")
            print("Mentega           =", round(resep_basePizza["Mentega (gram)"]*koefisien_basePizza),          "gram")
            print("Air               =", round(resep_basePizza["Air (ml)"]*koefisien_basePizza),                "gram")
            print("Garam             =", round(resep_basePizza["Garam (gram)"]*koefisien_basePizza),            "gram")
            print("Susu Bubuk        =", round(resep_basePizza["Susu Bubuk (gram)"]*koefisien_basePizza),       "gram")
            print("Bread Improver    =", round(resep_basePizza["Bread Improver (gram)"]*koefisien_basePizza),   "gram")
            print ("     ")
            input("Tekan enter untuk kembali ke menu...")    


    elif Pilihan_menu == "4":
            os.system('cls')
            
            teksRoti = ("ROTI BANTAL")
            teksRoti_tengah = teksRoti.center(75)
            print (teksRoti_tengah)
            
            graminasi = 30
            jumlahRotiBantal = 12

            print(f"Berikut ini merupakan daftar resep Roti Bantal")
            print(f"Untuk 12 Roti dengan Graminasi 150 gram/roti dan 1 roti terdiri dari 5 bulatan 30 gram \n")
            for bahan, jumlah in resep_rotiBantal.items():
                    print(f"{bahan:<20} = {jumlah:>5} gram ")
            print("     ")    
            while True:
                try:
                    banyakRoti_Bantal = int(input(f"Ingin membuat berapa roti Bantal?"))
                    break
                except ValueError:
                    print("Jawaban tidak valid, coba lagi")    

            print("     ")
            while True:
                try:
                    massaRoti_Bantal = int(input(f"Berapa graminasi setiap roti? (gram)"))
                    break
                except ValueError:
                    print("Jawaban tidak valid, coba lagi") 
            print("     ")    
            
            
            rumus_rotiBantal = graminasi*jumlahRotiBantal
            koefisien_rotiBantal = float((banyakRoti_Bantal*massaRoti_Bantal)/rumus_rotiBantal)
            bulatan = round(massaRoti_Bantal/5)
            print(f"Jadi untuk membuat roti Bantal sejumlah {banyakRoti_Bantal} dengan graminasi {massaRoti_Bantal} gram per roti, bahan bahan yang dibutuhkan adalah :")
            print("Tepung Terigu     =", round(resep_rotiBantal["Tepung Terigu (gram)"]*koefisien_rotiBantal),  "gram")
            print("Gula Pasir        =", round(resep_rotiBantal["Gula Pasir (gram)"]*koefisien_rotiBantal),     "gram")
            print("Ragi              =", round(resep_rotiBantal["Ragi (gram)"]*koefisien_rotiBantal),           "gram")
            print("Margarin          =", round(resep_rotiBantal["Margarin (gram)"]*koefisien_rotiBantal),       "gram")
            print("Air               =", round(resep_rotiBantal["Air (ml)"]*koefisien_rotiBantal),              "gram")
            print("Garam             =", round(resep_rotiBantal["Garam (gram)"]*koefisien_rotiBantal),          "gram")
            print("Susu Bubuk        =", round(resep_rotiBantal["Susu Bubuk (gram)"]*koefisien_rotiBantal),     "gram")
            print("Bread Improver    =", round(resep_rotiBantal["Bread Improver (gram)"]*koefisien_rotiBantal), "gram") 
            print("BOS / Mentega     =", round(resep_rotiBantal["BOS / Mentega (gram)"]*koefisien_rotiBantal),  "gram")
            print(f"\n Dengan catatan 1 roti terdiri dari 5 bulatan sebanyak {bulatan} gram \n")

            input("Tekan enter untuk kembali ke menu...")

    elif Pilihan_menu == "5":
            os.system('cls')
            
            teksRoti = ("RESEP ROTI BUNS BURGER")
            teksRoti_tengah = teksRoti.center(75)
            print (teksRoti_tengah)

            graminasi_buns = 68
            jumlahBuns = 22
            
            print(f"Berikut ini merupakan daftar resep Roti Buns Burger")
            print(f"Untuk 22 Roti dengan Graminasi 68 gram/roti \n")
            for bahan, jumlah in resep_bunsBurger.items():
                    print(f"{bahan:<20} = {jumlah:>5} gram ")

            print("     ")
            while True:   
                try:
                    banyakRoti_Buns = int(input(f"Ingin membuat berapa roti Buns?"))
                    break
                except ValueError:
                    print("Jawaban tidak valid, coba lagi")        

            print("     ")
            while True:   
                try:
                    massaRoti_Buns = int(input(f"Berapa graminasi setiap roti? (gram)"))
                    break
                except ValueError:
                    print("Jawaban tidak valid, coba lagi")
            print("     ")   
            
            rumus_rotiBuns = graminasi_buns*jumlahBuns
            koefisien_rotiBuns = float((banyakRoti_Buns*massaRoti_Buns)/rumus_rotiBuns)

            print(f"Jadi untuk membuat roti Buns sejumlah {banyakRoti_Buns} dengan graminasi {massaRoti_Buns} gram per roti, bahan bahan yang dibutuhkan adalah :")
            print("Tepung Terigu     =", round(resep_bunsBurger["Tepung Terigu (gram)"]*koefisien_rotiBuns),    "gram")
            print("Gula Pasir        =", round(resep_bunsBurger["Gula Pasir (gram)"]*koefisien_rotiBuns),       "gram")
            print("Ragi              =", round(resep_bunsBurger["Ragi (gram)"]*koefisien_rotiBuns),             "gram")
            print("Mentega           =", round(resep_bunsBurger["Mentega (gram)"]*koefisien_rotiBuns),          "gram")
            print("Air               =", round(resep_bunsBurger["Air (ml)"]*koefisien_rotiBuns),                "gram")
            print("Garam             =", round(resep_bunsBurger["Garam (gram)"]*koefisien_rotiBuns),            "gram")
            print("Susu Bubuk        =", round(resep_bunsBurger["Susu Bubuk (gram)"]*koefisien_rotiBuns),       "gram")
            print("Bread Improver    =", round(resep_bunsBurger["Bread Improver (gram)"]*koefisien_rotiBuns),   "gram") 
            print("BOS               =", round(resep_bunsBurger["BOS (gram)"]*koefisien_rotiBuns),              "gram")    

            input("Tekan enter untuk kembali ke menu...")
            
    elif Pilihan_menu == "6":            
            print("Terimakasih sudah menggunakan program ini")
            break
    
    elif Pilihan_menu != "1" or "2" or "3" or "4" or "5" or "6":
            print("Pilihan tidak tersedia!!")
            input("Tekan Enter untuk kembali ke menu...")
