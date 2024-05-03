import random

def rand_ip_gen(iplen=64):
    available_indexes = [i for i in range(iplen)]
    ip = [0] * iplen
    for i in range(iplen):
        randi = random.randint(0, len(available_indexes)-1)
        ip[i] = available_indexes.pop(randi)
    return ip

def get_ip_inverse(ip):
    iplen = len(ip)
    ip_inverse = [0] * iplen
    for i in range(iplen):
        ip_inverse[ip[i]] = i
    return ip_inverse

def print_ip(ip, w=8, h=8):
    for i in range(w):
        print(' & '.join(map(str, ip[i*8:i*8+8]))) 

def test():
    rand_ip = rand_ip_gen()
    ip_inverse = get_ip_inverse(rand_ip)
    
    print('-- IP')
    print_ip(rand_ip)

    print('-- IP Inverse')
    print_ip(ip_inverse)



