while True:
    number = list(map(int,input().split()))
    if number[0]==0 and number[1]==0 and number[2]==0:
        break
    elif (number[0]**2 == number[1]**2 + number[2]**2) or (number[1]**2 == number[2]**2 + number[0]**2) or (number[2]**2 == number[1]**2 + number[0]**2):
        print('right')
    else:
        print('wrong')