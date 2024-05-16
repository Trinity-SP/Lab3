weight = 57
height = 1.73

def calculate_bmi(height, weight): 
    print("Height = " + str(height)) 
    print("Weight = " + str(weight))
    
#Add code here to calculate BMI 
    BMI = (weight)/(height**2)

#Add code here to display calculate BMI
    print("Your BMI is " + str(BMI))

    if BMI < 18.5:
        print("Under Weight")
        return -1
    elif 18.5 <= BMI <= 25.0:
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1

calculate_bmi(weight=97, height=1.73)