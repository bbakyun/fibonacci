import time
"""
Implement fibonacci function that get k as a parameter, and return k-th fibonacci number.
For example, if k = 5, then the function fibonacci(5) should return 5
"""

def fibonacci1(k):
    """using iteration"""
    return 0

def fibonacci2(k):
    """using recursion"""
    return 0


def main():
    for i in range(20):
        print(fibonacci1(i+1))

    start = time.time()
    print("fibonacci1(100000): ", fibonacci1(100000))
    print("time of fibonacci1 : ", time.time() - start)

    start = time.time()
    print("fibonacci2(100000): ", fibonacci2(100000))
    print("time of fibonacci 2: ", time.time() - start)


if __name__ == "__main__":
    main()