def solution(s: str) -> int:
        
        res = 0

        my_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        previous = 0
        cur = 0
        
        for char in s:
            cur = my_dict[char]

            if cur > previous:
                res -= previous
            else:
                res += previous

            previous = cur
        
        res += previous

        return res