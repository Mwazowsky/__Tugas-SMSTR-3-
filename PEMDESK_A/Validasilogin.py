class Database:
    def __init__(self, max):
        self.max = max
        self.users = {}

    def Add_User(self, user, pwd):
        if len(self.users) < self.max:
            self.users[user] = pwd
            return "user berhasil terdaftar!!!"
        else:
            return "Database hanya mampu menampung 5 user, user tidak terdaftar"

    def Get_Validation(self, uname, passwrd):
        for i in self.users.keys():
            if i == uname and self.users[i] == passwrd:
                return True
        return False

    def View_Data(self):
        for i in self.users.items():
            print(i)

data_base = Database(5)

def Daftar():
    username = str(input("Masukkan username anda: "))
    password = str(input("Masukkan password anda: "))
    if username in data_base.users:
        print("Maaf Username harus unik, username anda " + username + " Tidak berhasil terdaftar")
    else:
        print(data_base.Add_User(username, password))

def Login():
    username = str(input("Masukkan username anda: "))
    password = str(input("Masukkan password anda: "))
    if data_base.Get_Validation(username, password) == True:
        return True
    else:
        return False

def Cek():
    data_base.View_Data()

exit = False

while exit == False:
    prompt = str(input("Selamat datang di portal pendaftaran SMA harapan bangsa(login/daftar/keluar): "))

    if prompt == "login":
        login_prompt = True
        attempt = 3
        while login_prompt == True and attempt > 0:
            if Login() == True:
                print("Login Berhasil!!!")
                input("Press Enter to continue...")
                login_prompt = False
            else:
                print("Login Gagal, username/password anda salah. Percobaan tersisa : " + str(attempt))
                print()
                lagi = str(input("Login Lagi(y/n)? "))
                if lagi == "y":
                    login_prompt = True
                    attempt -= 1
                else:
                    login_prompt = False

    elif prompt == "daftar":
        Daftar()

    elif prompt == "cek":
        Cek()

    elif prompt == "keluar":
        exit = True
