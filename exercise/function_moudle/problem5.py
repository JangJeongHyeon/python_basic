
def getBMI(height, weight):
    height = height / 100
    bmi = (weight/height**2)
    if(bmi < 18.5):
        print('마른체형')
    elif(18.5 <= bmi < 25.0):
        print('표준')
    elif(25.0 <= bmi < 30.0):
        print('비만')
    else:
        print('고도 비만')

if(__name__ == '__main__'):
    while(True):
        height = int(input('키를 입력하세요: '))
        weight = int(input('몸무게를 입력하세요: '))
        getBMI(height, weight)