limit = int(input())
speed = int(input())
if speed - limit >= 31:
    print("You are speeding and your fine is $500.")
elif 21 <= speed - limit <= 30:
    print("You are speeding and your fine is $270.")
elif 1 <= speed - limit <= 20:
    print("You are speeding and your fine is $100.")
else:
    print("Congratulations, you are within the speed limit!")