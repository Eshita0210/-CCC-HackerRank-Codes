n, k = map(int, input().split())
arr = list(map(int, input().split()))

# initialize a dictionary to keep track of the count of remainders
count = {}

# loop through the array and update the count of remainders
for i in range(n):
    rem = arr[i] % k
    if rem in count:
        count[rem] += 1
    else:
        count[rem] = 1

# initialize the number of pairs to 0
pairs = 0

# loop through the dictionary and count the number of pairs
for i in range(1, k//2+1):
    if i != k-i:
        pairs += count.get(i, 0) * count.get(k-i, 0)
    else:
        pairs += (count.get(i, 0) * (count.get(i, 0)-1)) // 2

# add the count of pairs with remainder 0
pairs += (count.get(0, 0) * (count.get(0, 0)-1)) // 2

# print the number of pairs
print(pairs)
