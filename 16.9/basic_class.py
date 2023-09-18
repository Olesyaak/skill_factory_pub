class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def return_str(self):
        return (str(self.side_1), str(self.side_2), str(self.side_3))

    def trianle_area(self):
        return self.side_1*self.side_2*self.side_3


class Wallet:
    def __init__(self, name, surname, amount):
        self.name = name
        self.surname = surname
        self.amount = amount

    def print_wallet(self):
        return (
            f'Клиент: {self.name} {self.surname}\
            Баланс: {self.amount} руб.'
            )


class Guests:
    def __init__(self, name, surname, city, status):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status

    def print_inf(self):
        return (
            f'{self.name} {self.surname} г.{self.city} статус {self.status}'
        )

# или вот так

class Guests_2:
    def __init__(self, name, surname, city, status):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status
