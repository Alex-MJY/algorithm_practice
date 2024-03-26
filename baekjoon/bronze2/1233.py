# 주사위 3개 S1(2 ≤ S1 ≤ 20), S2(2 ≤ S2 ≤ 20), S3(2 ≤ S3 ≤ 40)개의 면
s1, s2, s3 = map(int, input().split())
arr = [0] * (s1 + s2 + s3 + 1)
for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            arr[i + j + k] += 1
print(arr.index(max(arr)))