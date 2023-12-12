from functools import cmp_to_key

def compare_f(a, b):
    a_set, b_set = set(a), set(b)
    a_len, b_len = len(a), len(b)
    a_int, b_int = int(a), int(b)

    if a_len == b_len:
        if a_int > b_int:
            return -1
        elif a_int < b_int:
            return 1
        return 0
    
    if int(a + b) > int(b + a):
        return -1
    return 1


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())
    
    arr.sort(key=cmp_to_key(compare_f))
    print("".join(arr))

main()