
# Complete the compareTriplets function below.
def compareTriplets(a, b):
    calc = [(a[i] - b[i]) for i in range(0, len(a))]
    return [sum(c > 0 for c in calc), sum(c < 0 for c in calc)]

print(*compareTriplets([17, 28, 30], [99, 16, 8]))
