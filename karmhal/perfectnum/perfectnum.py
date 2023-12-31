# perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
def main():
    perfect()

def perfect():
    prompt = int(input("Bir sayi giriniz: "))
    divisors = []
    for i in range(1, prompt + 1):
        if prompt % i == 0:
            divisors.append(i)
    if sum(divisors) - prompt == prompt:
        print(f"{prompt} bir mukemmel sayidir.")
    else:
        print(f"{prompt} bir mukemmel sayi degildir.")

if __name__ == "__main__":
    main()
