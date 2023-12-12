from functools import cmp_to_key

def compare_f(a, b):
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