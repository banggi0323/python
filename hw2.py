def get_integer():
    payment = int(input("동전으로 교환하고자 하는 금액은? "))
    return payment

def exchange(amount):
    n500 = amount // 500
    amount %= 500

    n100 = amount // 100
    amount %= 100

    n50 = amount // 50
    amount %= 50

    n10 = amount // 10
    amount %= 10

    print(f'500원 동전의 개수: {n500}')
    print(f'100원 동전의 개수: {n100}')
    print(f'50원 동전의 개수: {n50}')
    print(f'10원 동전의 개수: {n10}')

amount = get_integer()
exchange(amount)
