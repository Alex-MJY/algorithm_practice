n = float(input())
while True:
    input_n = float(input())
    if input_n == 999:  break
    print(f"{input_n - n:.2f}")
    n = input_n