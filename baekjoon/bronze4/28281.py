n, x = map(int, input().split())
prices = list(map(int, input().split()))

array = []
for i in range(len(prices) - 1):
    array.append([i, prices[i] + prices[i + 1]])
values = [subarray[1] for subarray in array]
min_value = values.index((min(values)))

print((prices[min_value] * x) + (prices[min_value + 1] * x))