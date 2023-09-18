from basic_class import Triangle, Wallet, Guests, Guests_2

triangle_1 = Triangle(3, 4, 5)

print(triangle_1.return_str())
print(triangle_1.trianle_area())

wallet_1 = Wallet('Иван', 'Петров', 50)

print(wallet_1.print_wallet())

guests_1 = Guests('Иван', 'Иванов', 'Москва', 'Наставник')

print(guests_1.print_inf())

#или вот так

list_of_guest = []

def l_of_g():
    while True:
        name = input('Имя гостя или q для выхода: ')
        if name == 'q':
           break
        surname = input('Введите фамилию: ')
        city = input('Введите город: ')
        status = input('Введите статус: ')
        guest = Guests_2(name, surname, city, status)
        list_of_guest.append(guest)
    for g in list_of_guest:
        print(f'{g.name}, {g.surname}, г.{g.city}, статус {g.status}')

l_of_g()
