# king 1, queen 1, rook 2, bishop 2, knight 2, pawn 8

white_pieces = list(map(int, input().split()))
black_pices = [1, 1, 2, 2, 2, 8]
array = []

for i in range(len(white_pieces)):
    if white_pieces[i] == black_pices[i]:
        array.append(0)
    # elif white_pieces[i] < black_pices[i]:
    else:
        array.append(black_pices[i] - white_pieces[i])
        
for i in array:
    print(i, end=' ')