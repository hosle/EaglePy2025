import heapq
from typing import Counter


def sliceList():
    print("\n==== Slicing a list:")
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("0:5, ", lst[0:5])
    print("6:, ", lst[6:])
    print(":5, ", lst[:5])
    print("-5:, ", lst[-5:])
    print("-5:-1, ", lst[-5:-1])


def doCRUDList():
    print("\n==== Changing an item in a list:")

    # Construct a list list((a,a,a))
    myList = list(("a", "b", "c"))

    mylist2 = list(["a1", "b1", "c1"])

    print("mylist2:", mylist2)

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

    my_list_1 = []

    try:
        my_list_1.remove("c")
    except Exception as e:
        print("remove error: ", e)



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

    print("enumerate:")
    for index, item in enumerate(lst):
        print(index, "=", item)

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

    print("\n==== Enumerate a list:")

    simpleList = ["one", "two", "three"]

    print("Original simple list:", simpleList)

    # complexList = [(1, "one"), (2, "two"), (3, "three")]

    complexList = [(i + 1, v) for i, v in enumerate(simpleList)]

    print("Converted complex list:", complexList)

    print("Create a new list with only the second element of each tuple:")

    newlist = [x[1] for x in complexList]

    newlist2 = [x2 for _, x2 in complexList]

    print("Approach 1 : [x[1] for x in complexList] : ", newlist, ", type = ", type(newlist))
    print("Approach 2 : [x2 for x1, _ in complexList] : ", newlist2, ", type = ", type(newlist2))


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

    try:
        myMap["1"]
    except Exception as e:
        print("Error key not found : ", e)


    print("dict.items():", myMap.items())

    myMap["3"] = "ThreeString"

    print("[Add] After dict add '3'='TreeString':", myMap.items())

    myMap.update({4:"Four"})

    print("[Add] After myMap.update({4:'Four'}):", myMap.items())

    myMap.pop("3")

    print("[Remove] After myMap.pop('3'):", myMap.items())

    try:
        myMap.pop("3")

        print("[Remove] After myMap.pop('3'): ", myMap.items())
    except Exception as e:
        print("Error not found key when pop: ", e)


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

    print("[Loop] loop dict 2")
    for (key, value) in myMap.items():
        print(key, value)

    print()

    print("[Loop] loop dict by key")

    for key in myMap:
        print(key, myMap[key])


def useDictToCount():
    print("\n==== This is useDictToCount")

    myDict = {"apple": 1, "banana": 2, "cherry": 3}

    print("Original myList:", myDict)

    givenKey = "apple"

    givenKey2 = "orange"

    myDict[givenKey] = myDict.get(givenKey, 0) + 1

    print(f"after inspect {givenKey}, myDict is now:", myDict)

    myDict[givenKey2] = myDict.get(givenKey2, 0) + 1

    print(f"after inspect {givenKey2}, myDict is now:", myDict)


def create_new_dict_to_count_arr():
    # Example with a list of items
    data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    count = Counter(data)

    print(count)
    # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})


def use_heapq_to_sort_by_count():

    print("\n==== This is use_heapq_to_sort_by_count")

    arr = [1, 1, 1, 2, 2, 2, 3, 3, 5, 5, 5, 5]

    count_map = {}

    for item in arr:
        count_map[item] = count_map.get(item, 0) + 1

    heap = []

    for key, count in count_map.items():
        heapq.heappush(heap, (-count, key))

    max_freq, max_value = heapq.heappop(heap)

    print(f"value {max_value} has highest frequency {-max_freq}\n")


if __name__ == "__main__":
    # traverseListTupleSetDict()
    # doCRUDList()
    # doCRUDSet()
    # unionSet()
    # intersectionSet()
    # differenceSet()
    # symmetricDifferenceSet()

    # demo_map = {1: "One", 2: "Two"}
    # dictConstruction(demo_map)

    # dictLoop()

    use_heapq_to_sort_by_count()