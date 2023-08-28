"""

"""

def sol(phone_book):
    # 맨 앞자리가 1 인것부터 긴 순으로 정렬 [1, 123, 2, 234 ,...]
    phone_book = sorted(phone_book)

    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a) == True:
            return False
    return True

phone_book = ["1234", "456", "4567"]
print(sol(phone_book))