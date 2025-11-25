from fungsi import clear, pause
from data import jenis_senjata, model_senjata, semua_statistik
from prettytable import PrettyTable
import inquirer

def tampil_model():
    global jenis_senjata, model_senjata, semua_statistik
    while True:
        clear()
        print("=== DAFTAR JENIS SENJATA ===")

        pilihan_jenis = []
        for i in range(len(jenis_senjata)):
            pilihan_jenis.append(f"{i+1}. {jenis_senjata[i]}")
        pilihan_jenis.append(f"{len(jenis_senjata)+1}. Kembali")
        
        questions = [
            inquirer.List('pilihan',
                        message="Pilih jenis senjata",
                        choices=pilihan_jenis),
        ]
        
        answers = inquirer.prompt(questions)
            
        selected_jenis = answers['pilihan']
        
        if selected_jenis == (f"{len(jenis_senjata)+1}. Kembali"):
            return
            
        jenis = int(selected_jenis.split('.')[0]) - 1
        
        if jenis < len(jenis_senjata):
            clear()
            print(f"=== DAFTAR MODEL SENJATA {jenis_senjata[jenis].upper()} ===")

            pilihan_model = []
            for j in range(len(model_senjata[jenis])):
                pilihan_model.append(f"{j+1}. {model_senjata[jenis][j]}")
            pilihan_model.append(f"{len(model_senjata[jenis])+1}. Kembali")
            
            questions_model = [
                inquirer.List('pilihan_model',
                            message="Pilih model",
                            choices=pilihan_model),
            ]
            
            answers_model = inquirer.prompt(questions_model)
                
            selected_model = answers_model['pilihan_model']
            
            if selected_model == (f"{len(model_senjata[jenis])+1}. Kembali"):
                continue
                
            model = int(selected_model.split('.')[0]) - 1
            
            if model < len(model_senjata[jenis]):
                clear()
                
                print(f"=== STATISTIK {model_senjata[jenis][model].upper()} ===")
                stats = semua_statistik[jenis][model]
                
                table = PrettyTable()
                table.field_names = ["Statistik", "Nilai"]
                table.align["Statistik"] = "l"
                table.align["Nilai"] = "r"

                for k, v in stats.items():
                    table.add_row([k, v])

                print(table)
                pause()

        else:
            print("Jenis tidak valid!")
            pause()
