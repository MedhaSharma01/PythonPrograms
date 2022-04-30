
arr = [10, 20, 30, 40]
max = arr[0]
for i in range(0, len(arr)):
    if (arr[i] > max):
        max = arr[i]
print("Largest element " + str(max))
