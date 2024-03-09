def radix_sort(arr):
    max_digits = max([len(str(x)) for x in arr])
    b = 10
    bins = [[] for i in range(b)]
    for i in range(0, max_digits):
        print(str(i))
        for x in arr:
            digit = (x // b ** i) % b
            bins[digit].append(x)
        arr = [x for q in bins for x in q]
        print(arr)
        print(bins)
        bins = [[] for i in range(b)]
    return arr

