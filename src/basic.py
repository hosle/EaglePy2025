def traverseString():
    print("==== Traversing a string:")
    s = "hello world"
    for char in s:
        print(char, end=",")

    print("\n==== Traversing a string using index:")
    for i in range(len(s)):
        print(s[i], end=",")


def checkCharInString():
    print("\n==== Checking if substring is in string:")

    string = "this is a long string"
    keyword = "long"

    notKeyWord = "short"

    result = keyword in string

    print(f"string={string},", f"key={keyword},")

    print(f"Is {keyword} in string?", result)

    print(f"Is {notKeyWord} NOT in string?", notKeyWord not in string)


def sliceString():
    print("\n==== Slicing a string:")
    s = "12456789"
    print("0:5, ", s[0:5])
    print("6:, ", s[6:])
    print(":5, ", s[:5])
    print("-5:, ", s[-5:])
    print("-5:-1, ", s[-5:-1])


def removeWhitespace():
    print("\n==== Removing whitespace from a string:")
    s = "   hello world   "
    print(f"Original: '{s}'")
    print(f"Stripped: '{s.strip()}'")  # Removes leading and trailing whitespace
    print(f"Lstrip: '{s.lstrip()}'")  # Removes leading whitespace
    print(f"Rstrip: '{s.rstrip()}'")  # Removes trailing whitespace


def splitString():
    print("\n==== Splitting a string:")
    s = "apple, banana, cherry"
    fruits = s.split(", ")
    print(f"Original: '{s}'")
    print("Split:", fruits)  # Splits the string into a list of substrings


def replaceString():
    print("\n==== Replacing a substring in a string:")
    s = "hhhhaaaaaa"
    new_s = s.replace("a", "B")
    new_s2 = s.replace("a", "B", 2)  # Replaces only the first two occurrences of 'h'

    print(f"Original: '{s}'")
    print(f"Replaced: '{new_s}'")  # Replaces 'world' with 'Python'

    print(f"Replaced first two 'a's: '{new_s2}'")  # Replaces first two 'h's with 'b'

    print()


def startWithAndEndWith():
    print("\n==== Checking if a string starts with a substring:")
    s = "hello world"
    print(f"Does '{s}' start with 'hello'? {s.startswith('hello')}")
    print(f"Does '{s}' start with 'world'? {s.startswith('world')}")

    print("\n==== Checking if a string ends with a substring:")
    s = "hello world"
    print(f"Does '{s}' end with 'world'? {s.endswith('world')}")
    print(f"Does '{s}' end with 'hello'? {s.endswith('hello')}")


def sliceList():
    print("\n==== Slicing a list:")
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("0:5, ", lst[0:5])
    print("6:, ", lst[6:])
    print(":5, ", lst[:5])
    print("-5:, ", lst[-5:])
    print("-5:-1, ", lst[-5:-1])


def doCRUDList():
    print("\n==== Changing an item in a list:")

    # Construct a list list((a,a,a))
    myList = list(("a", "b", "c"))

    print("Original list:", myList)

    myList[0] = "replaced"

    print("Changed list:", myList)


    print("\n==== Adding an item to a list:")

    myList.append("d")

    print("List after appending 'd':", myList)


    print("\n==== Inserting an item into a list:")

    print("List before inserting 'x' at index 1:", myList)

    myList.insert(1, "x")

    print("List after inserting 'x' at index 1:", myList)


    print("\n==== Append another list to a list:")

    thisList = ["apple", "banana", "cherry"]

    tropical = ["mango", "pineapple", "papaya"]

    print("thisList before extending:", thisList)

    thisList.extend(tropical)

    print("thisList.extend(tropical) : ", thisList)

    thisTuple = ("kiwi", "orange")

    thisList.extend(thisTuple)

    print("Can extend any Iterable collections ", thisList)


    print("\n==== Removing an item from a list:")

    myList = ["a", "b", "c", "d", "e"]

    print("Original list:", myList)

    myList.remove("c")  # Removes the first occurrence of 'c'

    print("List after myList.remove('c') :", myList)

    myList.pop(1)

    print("List after myList.pop(1) the #1 element:", myList)


def traverseListTupleSetDict():
    print("\n==== Traversing a list:")
    lst = [1, 2, 3, 4, 5]

    print("Traversing a list using for item in lst:")
    for item in lst:
        print(item, end=",")
    print()  # For a new line after traversal

    print("Traversing a list using for i in range(len(lst)):")
    for i in range(len(lst)):
        print(lst[i], end=",")

    print()  # For a new line after traversal

    # same in tuple


    mySet = {"Set1", "Set2", "Set3", "Set4", "Set5"}

    print("==== Traversing a set by for it in mySet:")

    for it in mySet:
        print(it, end=",")


    print("\nTraversing a set using for item in mySet, need to cast to list if using index :")

    for i in range(len(mySet)):
        print(list(mySet)[i], end=",")

    print()


def listComprehension():
    print("\n==== List Comprehension:")

    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    print("Original list:", fruits)

    newlist = [x for x in fruits if "a" in x]

    print("Create new List which item has 'a' : ", newlist)


def sortList():
    print("\n==== Sorting a list:")

    lst = [5, 2, 9, 1, 5, 6]

    print("Original list:", lst)

    ascendingList = lst.copy()

    ascendingList.sort()

    print("Sorted ascending list:", ascendingList)

    descendingList = list(lst)

    descendingList.sort(reverse=True)

    print("Sorted descending list:", descendingList)

    print("Original list:", lst)


def doCRUDSet():
    print("\n==== CRUD a Set:")

    mySet = {"apple", "banana", "cherry"}

    print("Original Set:", mySet)

    mySet.add("orange")

    print("Set after mySet.add('orange'):", mySet)

    newSet = {"kiwi", "mango"}

    print("update another Set ", newSet)

    mySet.update(newSet)

    print("Set after mySet.update(newSet) with another set:", mySet)

    print("Remove an item from a set:")

    mySet.remove("banana")  # Raises KeyError if 'banana' is not found

    print("Set after mySet.remove('banana'):", mySet)

    mySet.discard("kiwi")  # Does not raise an error if 'kiwi' is not found

    print("Set after mySet.discard('kiwi'):", mySet)


def unionSet():
    print("\n==== Union of two sets:")

    set1 = {"apple", "banana", "cherry"}
    set2 = {"banana", "kiwi", "mango"}

    print("Original set1:", set1)
    print("Original set2:", set2)

    unionSet = set1.union(set2)

    print("Union of set1 and set2:", unionSet)

    set3 = {"watermelon", "peach"}

    unionSet.update(set3)

    print("Append set3 to unionSet by unionSet.update(set3):", unionSet)


def intersectionSet():
    print("\n==== Intersection of two sets:")

    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple"}
    print("Original set1:", set1)
    print("Original set2:", set2)

    set3 = set1.intersection(set2)
    print("set1.intersection(set2) : ", set3)


def differenceSet():
    set1 = {"a", "b", "c"}
    set2 = {"d", "e", "a"}

    print("Original set1:", set1)
    print("Original set2:", set2)

    set3 = set1.difference(set2)

    print("set1.difference(set2), create a new set contains those in set1 but not in set2, ", set3)


def symmetricDifferenceSet():
    set1 = {"a", "b", "c"}
    set2 = {"d", "e", "a"}

    print("Original set1:", set1)
    print("Original set2:", set2)

    set3 = set1.symmetric_difference(set2)

    print("set1.symmetric_difference(set2), create a new set contains those in either set1 or set2 but not both, ", set3)


def dictConstruction(myMap):
    print("\n==== This is dict construction ")

    print("this is key=1", myMap[1])

    if "1" in myMap:
        # if not check, throw error
        print("this is key='1'", myMap["1"])

    print("dict.items():", myMap.items())

    myMap["3"] = "ThreeString"

    print("[Add] After dict add '3'='TreeString':", myMap.items())

    myMap.update({4:"Four"})

    print("[Add] After myMap.update({4:'Four'}):", myMap.items())

    myMap.pop("3")

    print("[Remove] After myMap.pop('3'):", myMap.items())

    print("[Copy] Copy a dict to another dict")

    myMap2 = myMap.copy()

    print("myMap2 after myMap.copy():", myMap2.items())

    myMap3 = dict(myMap2)  # Another way to copy a dict
    if 3 in myMap3:
        myMap3.pop(3)

    if 2 in myMap3:
        myMap3.pop(2)

    print("myMap3 after dict(myMap2):", myMap3.items())

    print("myMap is still :", myMap.items())


def dictLoop():
    print("\n==== This is dictLoop")

    myMap = {
        1: "one",
        2: "two",
        # "1": "oneString"
    }
    print("[Loop] loop dict")
    for key, value in myMap.items():
        print(key, value)

    print()

    print("[Loop] loop dict by key")

    for key in myMap:
        print(key, myMap[key])

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


if __name__ == "__main__":

    print("==== String Basics ====")

    traverseString()

    checkCharInString()

    sliceString()

    removeWhitespace()

    splitString()

    replaceString()

    startWithAndEndWith()

    print("==== List ====")

    sliceList()

    doCRUDList()

    traverseListTupleSetDict()

    listComprehension()

    sortList()

    print("==== Set ====")

    doCRUDSet()

    unionSet()

    intersectionSet()

    differenceSet()

    symmetricDifferenceSet()

    print("==== Dict ====")
    #todo

    myMap = {
        1: "one",
        2: "two",
        # "1": "oneString"
    }

    dictConstruction(myMap)

    dictLoop()

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







