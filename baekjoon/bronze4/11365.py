while True:
    sentence = str(input())
    if sentence == "END":
        break
    print(sentence[::-1])