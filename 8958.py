a = int(input())

for _ in range(a):
    number = 0
    sum = 0
    t = input()
    for i in range(len(t)):
        if t[i] == 'O':
            number+=1
            sum+=number
        elif t[i] == 'X':
            number = 0
    print(sum)