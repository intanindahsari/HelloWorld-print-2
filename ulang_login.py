from fungsi import clear, pause
from login import login

def ulang_login():
    clear()
    username = input("Username: ")
    password = input("Password: ")
    status = login(username, password)
    if status == "":
        print("Username atau password salah! Coba lagi.\n")
        pause()
        return ulang_login()
    else:
        print(f"Berhasil login sebagai {status.upper()}!")
        pause()
        return status