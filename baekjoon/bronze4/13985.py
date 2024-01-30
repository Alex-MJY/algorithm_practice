array = []
s = input()
for i in s:
    if i.isalnum():
        array.append(i)
        
if int(array[0]) + int(array[1]) == int(array[2]):
    print("YES")
else:
    print("NO")