import random
from fungsi import clear, pause
from data import jenis_senjata, model_senjata

def menu_gacha():
    while True:
        clear()
        print("=== MENU GACHA SENJATA ===")
        print("1. Gacha Random")
        print("2. Gacha Pilih Class")
        print("3. Gacha 2x (1 Random + 1 Pilih Class)")
        print("4. Kembali")
        
        pilih = input("Pilih menu: ")
        
        if pilih == '1':
            clear()
            print("=== GACHA RANDOM ===")
            
            jenis = random.randint(0, len(jenis_senjata) - 1)
            model = random.randint(0, len(model_senjata[jenis]) - 1)
            senjata = model_senjata[jenis][model]
            
            print(f"Senjata: {senjata}")
            print(f"Jenis: {jenis_senjata[jenis]}")
            pause()
            
        elif pilih == '2':
            clear()
            print("=== GACHA PILIH CLASS ===")
            for i in range(len(jenis_senjata)):
                print(f"{i+1}. {jenis_senjata[i]}")
            
            try:
                pilih_class = int(input("Pilih class: ")) - 1
                if pilih_class >= 0 and pilih_class < len(jenis_senjata):
                    model = random.randint(0, len(model_senjata[pilih_class]) - 1)
                    senjata = model_senjata[pilih_class][model]
                    
                    print(f"\nSenjata: {senjata}")
                    print(f"Jenis: {jenis_senjata[pilih_class]}")
                else:
                    print("Pilihan tidak valid!")
            except ValueError:
                print("Input harus angka!")
            pause()
            
        elif pilih == '3':
            clear()
            print("=== GACHA PERTAMA (RANDOM) ===")
            
            jenis1 = random.randint(0, len(jenis_senjata) - 1)
            model1 = random.randint(0, len(model_senjata[jenis1]) - 1)
            senjata1 = model_senjata[jenis1][model1]
            
            print(f"Senjata: {senjata1}")
            print(f"Jenis: {jenis_senjata[jenis1]}")
            pause()
            
            clear()
            print("=== GACHA KEDUA (PILIH CLASS) ===")
            for i in range(len(jenis_senjata)):
                print(f"{i+1}. {jenis_senjata[i]}")
            
            try:
                pilih_class = int(input("Pilih class: ")) - 1
                if pilih_class >= 0 and pilih_class < len(jenis_senjata):
                    model2 = random.randint(0, len(model_senjata[pilih_class]) - 1)
                    senjata2 = model_senjata[pilih_class][model2]
                    
                    clear()
                    print("=== HASIL GACHA ===")
                    print(f"Senjata 1: {senjata1} ({jenis_senjata[jenis1]})")
                    print(f"Senjata 2: {senjata2} ({jenis_senjata[pilih_class]})")
                else:
                    print("Pilihan tidak valid!")
            except ValueError:
                print("Input harus angka!")
            pause()
            
        elif pilih == '4':
            break
        else:
            print("Pilihan tidak valid!")
            pause()
menu_gacha()