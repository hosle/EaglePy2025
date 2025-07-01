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


