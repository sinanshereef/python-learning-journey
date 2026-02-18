
#______BMI Calculator_________

#It should tell them the interpretation of their BMI based on the BMI value.
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.
print(f"""========================================
        BMI CALCULATOR
========================================""")

height=float(input('Enter your Height in Meter: '))
weight=float(input('Enter your weight in kilogram: '))

print('Calculating Your BMI...')
bmi=round(weight/(height**2),2)
print('========================================')
if bmi<18.5:
    print(f"your BMI is {bmi}")
    print('Health Status: You are Underweight')
elif bmi>=18.5 and bmi<25:
    print(f"Your BMI is {bmi}")
    print('Health Status: You have a Normal Weight')
elif bmi>=25 and bmi<30:
    print(f"Your BMI is {bmi}")
    print("Health Status: You are slightly Overweight")
elif bmi>=30 and bmi<35:
    print(f"Your BMI is {bmi}")
    print('Health Status: You are Obese')
else:
    print(f"Your BMI is {bmi}")
    print('Health Status:, You are Clinically Obese')
print(f"""========================================

Stay healthy and keep moving!""")