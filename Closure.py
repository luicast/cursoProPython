def makeMultiplayer(x) -> int:

    def multiplayer(n) -> int:
        return x * n
    
    return multiplayer

times1 = makeMultiplayer(10)
times2 = makeMultiplayer(4)

print(times1(3))
print(times2(5))
print(times1(times2(2)))