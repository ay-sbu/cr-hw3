


mapper = [32, 1, 2, 3, 4, 5, 
          4, 5, 6, 7, 8, 9, 
          8, 9, 10, 11, 12, 13, 
          12, 13, 14, 15, 16, 17, 
          16, 17, 18, 19, 20, 21, 
          20, 21, 22, 23, 24, 25, 
          24, 25, 26, 27, 28, 29, 
          28, 29, 30, 31, 32, 1]

def expansion(inp:list, expmapper) -> list:
    result = [0] * len(expmapper)
    for i in range(len(expmapper)):
        result[i] = inp[expmapper[i] - 1]
    return result

def test():
    global mapper
    num = 0x6A31E9FB
    bits_list = list(bin(num)[2:].zfill(32))
    print(''.join(map(str, bits_list)))
    result = expansion(bits_list, mapper)
    print(''.join(map(str, result)))


