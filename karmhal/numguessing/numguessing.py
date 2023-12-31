# computer should pick an random integer and then user should guess it
from random import randint

def main():
    rand()

def level():
    print("1-2-3 seviyelerini istediginiz zorluga göre secin")
    level = input("Seviye seciniz: ")

    if level == '1':
        return randint(1, 9)
    elif level == '2':
        return randint(10, 99)
    elif level == '3':
        return randint(100, 999)
    else:
        print("Geçersiz seviye seçimi. Lütfen 1, 2 veya 3 girin.")
        return level()

def rand():
    secretnum = level()

    while True:
        prompt = int(input("Sayiyi tahmin edin: "))
        if prompt > secretnum:
            print("Daha kucuk bir sayi girin")
        elif prompt < secretnum:
            print("Daha buyuk bir sayi girin")
        else:
            print("Tebrikler!")
            break

if __name__ == "__main__":
    main()
