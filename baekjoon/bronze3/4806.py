# 1
cnt = 0
try :
    while input() : cnt += 1
except :
    print(cnt)
    
'''
# 2
cnt = 0
while True:
    try:
        _ = input()
        cnt += 1
    except EOFError:
        break
print(cnt)

'''