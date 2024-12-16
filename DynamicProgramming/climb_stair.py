
def climb_stair(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    prev2, prev1 = 1, 2

    for i in range(3, n+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


if __name__ == "__main__":
    print(climb_stair(10))
    print(climb_stair(20))
    print(climb_stair(30))

