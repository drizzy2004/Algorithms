def roll_dice(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = 1

    for n in range(1, n + 1):
        for m in range(1, m + 1):
            dp[n][m] = sum(dp[n-1][m-x] for x in range(1, 7) if m-x >= 0)

    return dp[n][m]




if __name__ == "__main__":
    print(roll_dice(2,7))
    print(roll_dice(3,9))
    print(roll_dice(8,24))
