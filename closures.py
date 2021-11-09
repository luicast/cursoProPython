def makeRepeaterOf(n):
    def repeater(string):
        assert type(string) == str, "solo cadenas de caracteres"
        return string * n
    return repeater

def run():
    repeat = makeRepeaterOf(int(input("digite el numero de veces que se va a repetir la cadena: ")))
    print(repeat(input("digite una cadena de caractreres: ")))

if __name__ == "__main__":
    run()