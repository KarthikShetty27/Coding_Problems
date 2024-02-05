import math

def is_bleak(n):
    num = len(str(int(math.log(n, 10)))) + 1
    for i in range(n - num, n):
        if i + bin(i).count('1') == n:
            return 0
    return 1

def main():
    num = 3
    print(is_bleak(num))

if __name__ == "__main__":
    main()

