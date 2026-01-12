def int_to_byte_intarray():
    n = 4
    
    byte_strarray = bin(n)
    print(f"{byte_strarray=}")
    
    byte_intarray = [int(digit) for digit in bin(n)[2:]]
    
    print(f"{byte_intarray=}")


if __name__ == "__main__":
    
    int_to_byte_intarray()