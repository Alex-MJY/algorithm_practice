try:
    while True:
        name = input()
        for i in range(len(name)):
            if name[i] == 'i':
                print('e', end='')
            elif name[i] == 'e':
                print('i', end='')
            elif name[i] == 'I':
                print('E', end='')
            elif name[i] == 'E':
                print('I', end='')
            else:
                print(name[i], end='')
        print('\n', end='')
except:
    exit(0)