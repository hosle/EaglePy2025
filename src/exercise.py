
def sort_a_list() :
    list = [1,2,5,6,10]

    list.sort()

    print(f"list increasing : {list}")

    list.sort(reverse=True)

    print(f"list descending : {list}")


def count_by_map() :
    mylist = ['a', 'b', 'c', 'a', 'b']

    mymap = dict()

    for alpha in mylist :
        mymap[alpha] = mymap.get(alpha, 0) + 1

    for k,v in mymap.items():
        print(f"{k} appears {v} times")


def get_sub_string() :
    original = "this is an original string"

    print(f"original string = {original}")

    replace_a_word = original.replace("this", "that")

    print(f"remove 'this' {replace_a_word}")

    first_3 = original[3:]

    print(f"substring from index = 3 : {first_3}")


def remove_item_in_int_list() :
    mylist = list((2,1,3,4,5))

    print(f"ori = {mylist}")

    mylist.remove(2)

    print(f"remove item=2, {mylist}")

    mylist.pop(1)

    print(f"remove index=1, {mylist}")




if __name__ == "__main__":
    remove_item_in_int_list()

    sort_a_list()

    count_by_map()

    get_sub_string()

