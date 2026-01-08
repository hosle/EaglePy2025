
# add the least alphabets to the left of an input string, make it a palindrome string

def solution(input: str) -> str:
        reversed_input = input[::-1]

        # bcba
        # abcb
        n = len(input)
        i = 0
        while i < n:
            if input[:n-i] == reversed_input[i:]:
                break
            i += 1
        result = reversed_input[:i] + input[:]

        print("result: " + result)

        return result


# def test_case1():
#     assert "abcba" == solution("bcba")

# def test_case2():
#     assert "a" == solution("a")

# def test_case3():
#     assert "cabbac" == solution("bbac")

# def test_case4():
#     assert "abcba" == solution("abcba")

# if __name__ == "__main__":
#     test_case1()
#     test_case2()
#     test_case3()