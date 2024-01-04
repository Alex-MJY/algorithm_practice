counter = 0

while True:
    try:
        gum = input()
        counter += 1
    #except EOFError:
    except:
        break
print(counter)