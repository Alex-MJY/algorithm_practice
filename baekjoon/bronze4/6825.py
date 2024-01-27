weight = float(input())
height = float(input())
bmi = weight / (height * height)
if bmi > 25:
    print("Overweight")
elif 25 >= bmi >= 18.5:
    print("Normal weight")
else:
    print("Underweight")