for _ in range(int(input())):
    case = input()
    counter = 0
    for i in case:
        if i == 'U':
            counter += 1
        else:
            break
    print(counter)