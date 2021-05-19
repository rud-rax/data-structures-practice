import math


def division_method(key,table_len = 10):
    return key % table_len

def multiplicative_hash_function(key,m = 50,a = 0.61803398987):
    if 0 < a < 1:
        hash = float(key * a)
        hash = math.modf(hash)[0]
        hash = int(m * hash)
        return hash

def extraction_hash_function(key,*postions):
    str_key = str(key)
    hash = 0
    for i in postions:
        hash *= 10
        hash += int(str_key[i])
    return hash


def mid_square(key):
    str_key = str(key ** 2)
    len_key = len(str_key)
    mid_key = len_key // 2
    hash = int(str_key[mid_key-1:mid_key + 2])
    return hash


def folding(key):
    pass

def universal_hashing(key): pass


if __name__ == "__main__": 

  print(mid_square(int("712")))

