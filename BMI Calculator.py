logo = """

   ______    __     __)    _____   )   ___                                
  (, /    ) (, /|  /|     (, /    (__/_____)     /)        /)             
    /---(     / | / |       /       /       _   // _      // _  _/_ _____ 
 ) / ____) ) /  |/  |_  ___/__     /       (_(_(/_(__(_(_(/_(_(_(__(_)/ (_
(_/ (     (_/   '     (__ /       (______)                                

"""
print(logo)

import random

def calculate_bmi(weight, height):
    """
    Function to calculate BMI
    :param weight: Weight in kilograms
    :param height: Height in meters
    :return: BMI value
    """
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """
    Function to determine the BMI category
    :param bmi: BMI value
    :return: BMI category as a string
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")

    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()
