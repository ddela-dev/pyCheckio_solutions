def largest_histogram(histogram):
    if len(histogram) == 1:
        return histogram[0]
    maxsq=0
    for i in range(1,max(histogram) + 1):
        current=0
        for h in histogram:
            if h >= i:
                current+=i
            else:
                if current > maxsq:
                    maxsq = current
                current=0
        if current>maxsq:
            maxsq=current
    return maxsq


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
