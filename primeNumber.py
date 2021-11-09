def isPrime(number:int) -> bool:
    result = [x for x in range(2, number) if number % x == 0]
    return len(result) == 0


def run():
    number:int = int(input(" digite un numero: "))
    isPrime(number)
    if isPrime(number) != False:
        print(f" el numero {number} es un numero primo")
    else:
        print(f"el numero {number} no es un numero primo")


if __name__ == "__main__":
    run()