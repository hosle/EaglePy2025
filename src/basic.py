import basic_str
import basic_collection
import basic_sorting


def ifStatement():
    print("\n==== if statement:")

    x = 6

    if x > 5:
        print("if elif: x is greater than 5")
    elif x == 5:
        print("x is equal to 5")
    else:
        print("x is less than 5")


    if x > 5 & x < 10:
        print("if and : x in between 5 and 10")

    match x:
        case 1:
            print("match : x is 1")
        case 2:
            print("match : x is 2")
        case _:
            print("match x : x is something else, not 1 or 2")


def whileloop():
    print("\n==== while loop:")

    i = 0
    while i < 6:
        i += 1

        if i == 3:
            print("continue when i is ", i)
            continue
        else:
            print("i is:", i)

        if i == 4:
            print("break when i is ", i)
            break


    print("\n---- for loop with range, step 3:")

    for x in range(2, 30, 3):
        print(x, end=", ")


class Car:
    def __init__(self, owner):
        self.owner = owner

    def drive(self, destination):
        print(f"{self.owner} is driving the car to {destination}.")

def classObjects():
    car = Car("Alice")

    print("[member variable] self.owner =", car.owner)

    print("[member method] execute car.drive(): ")

    car.drive("home")


def getBiggerNum(a:int, b:int) -> int:
    if a > b:
        return a
    else:
        return b


def swap(a, b):
    print(f"Swapping values: a={a}, b={b}")

    a, b = b, a

    print(f"After swap: a={a}, b={b}")


if __name__ == "__main__":

    print("==== String Basics ====")

    basic_str.traverseString()

    basic_str.checkCharInString()

    basic_str.alphabetChar()

    basic_str.sliceString()

    basic_str.removeWhitespace()

    basic_str.splitString()

    basic_str.replaceString()

    basic_str.startswith_And_endswith()

    print("==== List ====")

    basic_collection.sliceList()

    basic_collection.doCRUDList()

    basic_collection.traverseListTupleSetDict()

    # like the filter a list to make another new list with lambda applied to each item
    basic_collection.listComprehension()

    basic_collection.sortList()

    print("==== Set ====")

    basic_collection.doCRUDSet()

    basic_collection.unionSet()

    basic_collection.intersectionSet()

    basic_collection.differenceSet()

    basic_collection.symmetricDifferenceSet()

    print("==== Dict ====")

    myMap = {
        1: "one",
        2: "two",
        # "1": "oneString"
    }

    basic_collection.dictConstruction(myMap)

    basic_collection.dictLoop()

    basic_collection.useDictToCount()

    basic_collection.use_heapq_to_sort_by_count()

    print("==== if statement ====")

    ifStatement()

    print("==== loop ")

    whileloop()


    print("==== json handling ====")
    #todo
    #json.loads()
#     json.dumps()

    print("==== Class and objects ====")
    classObjects()

    print("==== python3 function ====")
    print("getBiggerNum ", getBiggerNum(3, 5))

    print("==== sorting ====")

    basic_sorting.sortingList()

    basic_sorting.sortingDict()

    basic_sorting.sortingTuple()

    print("==== swap ====")

    swap(10, 20)







