from fungsi import clear, pause
from data import rekomendasi_list, semua_statistik
from prettytable import PrettyTable
from colorama import Fore, Style, init

init(autoreset=True)

def tampil_statistik(jenis, model):
    clear()
    
    print(Fore.YELLOW + "=== STATISTIK SENJATA " + rekomendasi_list[jenis][model] + " ===" + Style.RESET_ALL)
    
    stats = semua_statistik[jenis][model]
    
    table = PrettyTable()
    table.field_names = ["Statistik", "Nilai"]
    table.align["Statistik"] = "l"
    table.align["Nilai"] = "r"

    for k, v in stats.items():
        table.add_row([k, v])

    print(table)
    pause()