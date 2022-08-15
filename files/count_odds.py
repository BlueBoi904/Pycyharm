def count_odds(low, high):
    ret = (high - low) // 2
    if (high % 2) == 1 or (low % 2) == 1:
        ret += 1
    return ret


print(count_odds(3, 7))
