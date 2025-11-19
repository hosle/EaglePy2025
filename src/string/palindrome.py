

def solution(str):
    print()
    print(f"original: {str}")

    j = len(str)
    shortpg = 1

    while j > 0:
        if is_palindrome(str[:j]):
            shortpg = j
        j -= 1

    # print(f"palindrome index ={shortpg}")

    if shortpg == len(str):
        print(f"result: {str}")
        return

    result = str
    for j2 in range(shortpg, len(str)):
        result = str[j2] + result

    print(f"result: {result}")


def is_palindrome2(str):
    i = 0
    j = len(str) - 1

    while i <= j:
        if str[i] == str[j]:
            i += 1
            j -= 1
        else:
            break
    return i >= j


def is_palindrome(str):
    if len(str) == 1:
        return False

    i = 0
    j = len(str)-1

    while i < j:
        if str[i] == str[j]:
            i += 1
            j -= 1
        else:
            break

    return i >= j


if __name__ == "__main__":
    solution("ABAC")
    solution("BC")
    solution("AB")
    solution("ABA")

    assert not is_palindrome2("ABAC")
    assert is_palindrome2("ABA")
    assert is_palindrome2("ABCBA")
    assert is_palindrome2("ABCCBA")