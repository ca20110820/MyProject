
def insertion_sort(numbers):
    # Reference: https://www.shiksha.com/online-courses/articles/insertion-sort-algorithm-with-code/
    for i in range(1, len(numbers)):
        k = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > k:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = k

    return numbers
