def makeDivBy(n:int)-> float:
    def div(x:int):
        assert n != 0, "no puedes dividir entre cero"
        return x/n
    return div

def run():
    division: int = makeDivBy(int(input("digite un numero: ")))
    print(division(int(input("digite otro numero: "))))

if __name__ == "__main__":
    run()