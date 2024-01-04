array = []

while True:
    number = int(input())
    if number == 0:
        break
    array.append(number)
    if number % 42 == 0:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
    
# for i in array:
#     if i % 42 == 0:
#         print("PREMIADO")
#     else:
#         print("TENTE NOVAMENTE")