def buy(shopping_bag):
    print('[구입]')
    item = input('상품명? ')
    if item == '':
        print()
        return False
    num = int(input('수량은? '))
    shopping_bag[item] = num
    print(f'장바구니에 {item} {num}개가 담겼습니다.')
    print()
    return True

def show(shopping_bag):
    print('>>> 장바구니 보기:', shopping_bag)
    print()

def find(shopping_bag):
    print('[검색]')
    key = input('장바구니에서 확인하고자 하는 상품은? ')
    if key in shopping_bag:
        print(f'{key}은(는) {shopping_bag[key]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {key}은(는) 없습니다.')
    print()

shopping_bag = {}

while True:
    if not buy(shopping_bag):
        break

show(shopping_bag)
find(shopping_bag)
find(shopping_bag)
