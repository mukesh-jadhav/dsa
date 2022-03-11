# problem:
    # given an array of coins, return minimum amount of change that you can not create from them.
    # e.g. coins = [1, 2, 5] the minimum amount of change you can not create is 4.

# logic:
    # iterate on items, keep summing them up one at a time,
    # you can not create previous_sum + 1 if previous_sum + 1 < current_coin

# O(nlog(n)) time O(1) space
def minimumNonConstructibleChange(coins):
    coins.sort()
    possible_change = 0
    for coin in coins:
        if coin > possible_change + 1:
            return possible_change + 1
        possible_change += coin
    return possible_change + 1


if __name__ == "__main__":
    coins = [1, 2, 3]
    print(minimumNonConstructibleChange(coins))


