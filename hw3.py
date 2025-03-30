def get_fixed_price(discount_rate, discounted_price):
    price = discounted_price / (1 - discount_rate / 100)
    return int(price)

discount_rate = int(input("할인율은? "))

A_discounted = int(input("A 상품의 할인된 가격은? "))

B_discounted = int(input("B 상품의 할인된 가격은? "))

A_price = get_fixed_price(discount_rate, A_discounted)
B_price = get_fixed_price(discount_rate, B_discounted)

print(f"A 상품의 정가는 {A_price}원")
print(f"B 상품의 정가는 {B_price}원")
