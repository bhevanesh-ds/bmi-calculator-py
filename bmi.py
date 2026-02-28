def bmi_metric():
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your weight in centimeters (cm): "))
    height_m = height/100   #converting height from centimeters into meters
    bmi = round(float(weight/(height_m*height_m)), 2)
    print("BMI: ", bmi)
    
    #BMI Classifications and health risk levels

    if bmi < 18.5:
        print("Classification: Underweight")
        print("Health risk: Low")
    elif 18.5 <= bmi < 25:
        print("Classification: Normal weight")
        print("Health risk: Average")
    elif 25 <= bmi < 29.9:
        print("Classification: Overweight")
        print("Health risk: Mildly increased")
    elif 30 <= bmi < 34.9:
        print("Classification: Obese Class 1")
        print("Health risk: Moderate")
    elif 35 <= bmi < 39.9:
        print("Classification: Obese Class 2")
        print("Health risk: Severe")
    elif 40 < bmi:
        print("Classification: Obese Class 3")
        print("Health risk: Very Severe")
    else:
        print("System error or incorrect BMI values. Please retry.")

    # Defining weight to be lost

    normal_weight = float(24*height_m*height_m)
    weight_diff = round(float(weight-normal_weight), 2)
    if weight_diff > 10:
        print("You need to loose ", weight_diff, "kilograms.")
    elif 0 < weight_diff <= 10:
        print("Your weight is perfect. Try to maintain it!!!")
    elif weight_diff < 0:
        print("You need to gain ", abs(weight_diff), "kilogram
