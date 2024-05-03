

def permute(s:list): # len(s) = len(p) = len(p)
    p = [
        16, 7  ,20 ,21, 29, 12, 28 ,17,
        1  ,15 ,23 ,26, 5  ,18 ,31 ,10,
        2  ,8  ,24 ,14 ,32 ,27 ,3,  9,
        19, 13, 30, 6,  22, 11, 4 , 25,
    ]
    
    result = [0] * len(s)
    for i in range(len(s)):
        result[p[i] - 1] =  s[i]
    
    return result

def test():
    s = list('00010110000111000110011011010111')
    result = permute(s)
    print(''.join(map(str, result)))