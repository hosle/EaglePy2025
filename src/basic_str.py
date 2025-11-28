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


def next_char(c) -> str:
    if c == 'z':
        return 'a'

    elif c == 'Z':
        return 'A'

    else:
        return chr(ord(c) + 1)


def alphabetChar():
    print("\n==== alphabet character to integer:")

    char = 'a'
    print(f"Character '{char}' to integer:", ord(char))  # ord() converts character to its ASCII value

    print("==== integer to alphabet character:")

    num = 97
    print(f"Integer {num} to character:", chr(num))  # chr() converts ASCII value back to character

    print(f"==== next character in alphabet:")
    next_char_result = next_char(char)
    print(f"Next character after '{char}' is '{next_char_result}'")



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


def startswith_And_endswith():
    print("\n==== Checking if a string starts with a substring:")
    s = "hello world"
    print(f"Does '{s}' start with 'hello'? {s.startswith('hello')}")
    print(f"Does '{s}' start with 'world'? {s.startswith('world')}")

    print("\n==== Checking if a string ends with a substring:")
    s = "hello world"
    print(f"Does '{s}' end with 'world'? {s.endswith('world')}")
    print(f"Does '{s}' end with 'hello'? {s.endswith('hello')}")


def reverse_string():
    print("\n ==== reverse a string")

    s = "hello world"

    reversed_s = s[::-1]

    print("origin string: ", s)

    print("reverse string: ", reversed_s)


if __name__ == "__main__":
    reverse_string()
    sliceString()