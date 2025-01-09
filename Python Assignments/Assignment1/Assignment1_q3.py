
def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Body Mass Index Calculator")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Please enter a positive number.")
            return
        
        bmi = calculate_bmi(weight, height)

        category = bmi_category(bmi)

        print("Your BMI is: ", bmi)

        print("You are: ", category)

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()