

def calBMI(height, weight):
    height = height / 100
    bmi = (weight / height**2)

    if( bmi < 18.5):
        print('마른체형')
    elif(18.5 <= bmi < 25.0):
        print('표준')
    elif(25.0 <= bmi < 30.0):
        print('비만')
    elif( bmi >= 30.0):
        print('초고도비만')
    

calBMI(170, 80)
