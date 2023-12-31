# between 1-150 if 3 can divide the number write fizz, if 5 write buzz, if both write fizzbuzz

def main():
    fizzbuzz()

def fizzbuzz():
    for sayi in range(1, 151):
        if sayi % 3 == 0 and sayi % 5 == 0:
            print("FizzBuzz")
        elif sayi % 3 == 0:
            print("Fizz")
        elif sayi % 5 == 0:
            print("Buzz")
        else:
            print(sayi)

if __name__ == "__main__":
    main()
    