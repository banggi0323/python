def read_single_digit(d):
    if d == '0':
        return "영"
    elif d == '1':
        return "일"
    elif d == '2':
        return "이"
    elif d == '3':
        return "삼"
    elif d == '4':
        return "사"
    elif d == '5':
        return "오"
    elif d == '6':
        return "육"
    elif d == '7':
        return "칠"
    elif d == '8':
        return "팔"
    elif d == '9':
        return "구"

def read_number(num):
    if len(num) == 1:
        print(read_single_digit(num[0]))
    elif len(num) == 2:
        print(read_single_digit(num[0]), read_single_digit(num[1]))
    elif len(num) == 3:
        print(read_single_digit(num[0]), read_single_digit(num[1]), read_single_digit(num[2]))

num = input("세 자리 정수 입력: ")
read_number(num)
