for i in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    start = (sh * 3600) + (sm * 60) + ss
    end = (eh * 3600) + (em * 60) + es
    time = end - start
    h = time // 3600
    m = (time % 3600) // 60
    s = (time % 3600) % 60
    
    print(h, m, s)