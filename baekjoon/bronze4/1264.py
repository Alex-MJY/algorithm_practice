while True:
    s = str(input())
    
    if s == "#":
        break
    counter = 0
    for i in s.lower():
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            counter += 1
    print(counter)