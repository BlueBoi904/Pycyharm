def count_odds(low, high):
    odd_count = 0
    for i in range(low, high + 1):
        if i % 2 != 0:
            odd_count += 1
    return odd_count


print(count_odds(3, 7))
