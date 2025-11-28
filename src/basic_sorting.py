def sortingList():
    print("\n==== sorting list")

    origin = [(1,"one"), (10, "ten"), (4, "four")]
    print("origin list : ", origin)

    origin.append((2,"Two"))
    print("After adding element 2: ", origin)

    sortedList = sorted(origin, key= lambda x : x[0])

    print("new sortedList by sorted(): ", sortedList)


    origin.sort(key= lambda it : it[0])

    print("In place sorting List origin : ", origin)


def sortingDict():
    print("\n==== Sorting Dict")

    myDict = dict({
        1: "One",
        8: "Eight",
        2: "Two"
    })

    print("Origin dict: ", myDict)

    sortedDict = dict(sorted(list(myDict.items())))

    print("sorted Dict: dict -> list -> sort -> dict :", sortedDict)


def sortingTuple():
    print("\n==== Sorting Tuple")

    myTuple = tuple((
        3,
        5,
        10,
        2,
        100
    ))

    print("origin tuple: ", myTuple)
    print("tuple to list: ", list(myTuple))

    sortedTuple = tuple(sorted(list(myTuple)))

    print("sorted tuple: tuple -> list -> sort -> tuple :", sortedTuple)

if __name__ == "__main__":
    # sortingTuple()
    sortingList()