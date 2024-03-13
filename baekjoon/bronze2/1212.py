if __name__ == "__main__":
    oct_input = input()
    decimal_num = int(oct_input, 8)
    binary_num = bin(decimal_num)
    print(binary_num[2:])
    