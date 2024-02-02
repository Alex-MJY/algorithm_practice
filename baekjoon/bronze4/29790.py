n, u, l = map(int, input().split())

# sign = 0
# # if n >= 1000:
# #     sign = 1
# # else:
# #     print("Bad")

if n < 1000:
    print("Bad")
elif n >= 1000 and (u >= 8000 or l >= 260):
    print("Very Good")
else:
    print("Good")