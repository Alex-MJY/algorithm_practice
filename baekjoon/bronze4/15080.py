start = list(map(str, input().split(' : ')))
end = list(map(str, input().split(' : ')))

start_sec = (int(start[0]) * 3600) + (int(start[1]) * 60) + int(start[2])
end_sec = (int(end[0]) * 3600) + (int(end[1]) * 60) + int(end[2])

if end_sec < start_sec:
    result = (24 * 3600) - start_sec + end_sec
else:
    result = end_sec - start_sec
print(result)