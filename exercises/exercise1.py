print("Welcome to the BMI calculator")

user_weight = float(input("Provide above your weight: "))
user_height = float(input("Provide above your height: "))
BMI = user_weight / (user_height**2)

print(f"According to your weight: {user_weight} and your height: {user_height}. Your BMI is: {BMI}")
