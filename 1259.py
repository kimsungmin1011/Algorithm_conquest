while True:
    n = input()  # 문자열로 입력 받기
    if n == "0":  # 0이 입력되면 종료
        break
    if n == n[::-1]:  # 문자열을 거꾸로 읽은 것과 원래 문자열이 같은지 확인
        print("yes")
    else:
        print("no")