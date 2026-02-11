# Grab interview
# 
# given binary string S = "111011", if odd, abstract 1, if even, divided by 2, 
# return the step num when S reduced to be 0

def solution2(s):
    print("solution2")
    # Solution2 time cost : 53.54248094558716
    count = 0
    s_int = int(s, 2)
    
    while s_int > 0:
        count += 1
        if s_int % 2 == 1:
            s_int -= 1
        else:
            s_int = s_int // 2
    
    print(f"result : {count}")

    return count
    
        

def solution(s):
    print("solution")
    
    if not "1" in s:
        return 0
    # 1111
    step = 0
    
    pre_zero = 0
    
    for item in s:
        if item == "0":
            pre_zero += 1
        else:
            break
    
    # print(f"{pre_zero=}")
    
    for i in range(pre_zero+1, len(s)):
        # print(f"{i=}, {s[i]=}")
        if s[i] == "1":
            step += 2
        else:
            step += 1
        
    print(f"result : {step + 1}")
    return step + 1