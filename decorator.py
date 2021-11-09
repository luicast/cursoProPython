from datetime import datetime

def executionTime(func):
    def wrapper(*args, **kwargs):
        initialTime = datetime.now()
        func(*args, **kwargs)
        finalTime =  datetime.now()
        timeElapsed:float = finalTime - initialTime
        print(f"pasaron {timeElapsed.total_seconds()} segundos")
    return wrapper


@executionTime
def randomFunc():
    for _ in range(1, 100000000):
        pass


@executionTime
def suma(a:int, b:int) ->int:
    return a + b


@executionTime
def saludo(nombre = "cesar"):
    print(f"hola {nombre}")


suma(5,5)
randomFunc()
saludo("luis")