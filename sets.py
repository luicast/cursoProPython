# [1,1,2,2,4] -> [1,2,4]

def removeDuplicate(someList):
    withoutDuplicate = []
    for element in someList:
        if element not in withoutDuplicate:
            withoutDuplicate.append(element)
    return withoutDuplicate


def delDuplicates(someList):
    return list(set(someList))


def run():
    randomList = [1,1,2,2,4]
    print(removeDuplicate(randomList))
    print(delDuplicates(randomList))


if __name__ == "__main__":
    run()