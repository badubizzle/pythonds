def sum_min_max(array, iterations):
    if len(array) <= 0:
        return 'Empty list'

    if iterations < 1:
        return 'No additions made'

    if iterations > len(array):
        return 'Iteration is out of scope'

    array.sort()

    count = 0
    min_sum = 0
    max_sum = 0

    for front, back in zip(array, array[::-1]):
        if count < iterations:
            min_sum += front
            max_sum += back
            count += 1

    return (min_sum, max_sum)


values = [5, 6, 4, 8, 10, 11, 15]
# values = []

print(sum_min_max(values, 1))
print(sum_min_max(values, 2))
print(sum_min_max(values, 3))
print(sum_min_max(values, 4))
print(sum_min_max(values, 5))
print(sum_min_max(values, 6))
print(sum_min_max(values, 7))
print(sum_min_max(values, 8))
print(sum_min_max(values, 9))
print(sum_min_max(values, 0))
