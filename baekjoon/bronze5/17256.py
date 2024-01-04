ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

array = [cx - az, cy // ay, cz - ax]
print(*array)