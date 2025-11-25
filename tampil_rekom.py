from fungsi import clear, pause
from data import jenis_senjata
from tampil_model_rekom import tampil_model_rekomendasi
import inquirer

def tampil_rekomendasi():
    while True:
        clear()
        print('=== REKOMENDASI SENJATA ===')

        pilih_jenis = []
        for i in range(len(jenis_senjata)):
            pilih_jenis.append(f"{i+1}. {jenis_senjata[i]}")
        pilih_jenis.append(f"{len(jenis_senjata)+1}. Kembali")

        questions = [
            inquirer.List('pilih_jenis',
                        message="Pilih jenis senjata",
                        choices=pilih_jenis),
        ]

        answers = inquirer.prompt(questions)
        
        selected_jenis = answers['pilih_jenis']

        if selected_jenis == (f"{len(jenis_senjata)+1}. Kembali"):
            return
        
        pilih = int(selected_jenis.split('.')[0]) - 1

        if pilih < len(jenis_senjata):
            tampil_model_rekomendasi(pilih)
        elif pilih == len(jenis_senjata):
            break
        else:
            print("Pilihan tidak valid!")
            pause()
