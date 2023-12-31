# I should check user's input
    # for username and password
# I can use regular expressions
import re

def main():
    username()
    password()

def username():
    while True:
        username = input("Kullanici adinizi giriniz: ")
        regex = "^[A-Za-z]\\w{4,14}$"
        r = re.compile(regex)
        if not (re.search(r, username)):
            print(
                "Kullanici adi 5-15 karakter arasi olmali, '_' disinda yabanci karakter bulundurmamali."
            )
        else:
            break

def password():
    while True:
        password = input("Sifrenizi giriniz: ")
        regex = "(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,})"
        r = re.compile(regex)
        if re.search(r, password):
            print("Guclu Sifre")
            break
        else:
            print("Zayif Sifre")
            continue

if __name__ == "__main__":
    main()
