
def max_rating_row(hits):
    """
    Check max row for one of top-10 in bookmakers
    rating in a row
    """
    current_row = 0
    max_row = 0
    for hit in hits:
        if hit <= 10:
            current_row += 1
            if max_row < current_row:
                max_row = current_row
        else:
            current_row = 0
    return max_row


# print(max_rating_row([11, 12, 13, 1, 2, 3, 15, 1, 2, 3, 4]))
# print(max_rating_row([11, 12, 13, 1, 2, 3, 4, 5, 15, 1, 2, 3, 4]))
#
# print(max_rating_row([11, 12, 13, 1, 2, 3, 15]) )
# print(max_rating_row([11, 12, 13, 1, 2, 3]))
# print((max_rating_row([1, 15])))
# print(max_rating_row([15]) )