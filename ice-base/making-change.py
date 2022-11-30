def checkio(price, den):
    if price == 0:
        return 0
    if min(den) > price:
        return None
    dp = [-1]
    for d in range(price):
        dp.append(-1)
    for i in den:
        if i > len(dp) - 1:
            continue
        dp[i] = 1
        for j in range(i + 1, price + 1):
            if dp[j - 1] == -1:
                continue
            elif dp[j] == -1:
                dp[j] = dp[j - i] + 1
            else:
                dp[j] = min(dp[j], dp[j - i] + 1)
    if dp[price] == 0:
        return None
    return dp[price]


if __name__ == '__main__':
    print("Example:")
    print(checkio(8, [1, 3, 5]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    print('Done')
