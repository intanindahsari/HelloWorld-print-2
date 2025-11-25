from fungsi import clear, pause
from data import jenis_senjata, rekomendasi_list
from tampil_stat import tampil_statistik
import inquirer

def tampil_model_rekomendasi(pilih_jenis):
    while True:
        clear()
        print(f"REKOMENDASI {jenis_senjata[pilih_jenis].upper()}:")

        pilih_model = []
        for j in range(len(rekomendasi_list[pilih_jenis])):
            pilih_model.append(f"{j+1}. {rekomendasi_list[pilih_jenis][j]}")
        pilih_model.append(str(len(rekomendasi_list[pilih_jenis])+1) + ". Kembali")

        questions_model = [
            inquirer.List('pilih_model',    
                        message="Pilih model untuk lihat statistik",
                        choices=pilih_model),
        ]

        answers_model = inquirer.prompt(questions_model)

        selected_model = answers_model['pilih_model']

        if selected_model == (str(len(rekomendasi_list[pilih_jenis])+1) + ". Kembali"):
            return
        
        pilih_model = int(selected_model.split('.')[0]) - 1

        if pilih_model < len(rekomendasi_list[pilih_jenis]):
            tampil_statistik(pilih_jenis, pilih_model)
        elif pilih_model == len(rekomendasi_list[pilih_jenis]):
            break
        else:
            print("Pilihan tidak valid!")
            pause()