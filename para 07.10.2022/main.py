class Citizen:
    def __init__(self, name, surname, birth_date):
        #birth_date is a string (Example: 2022/10/7
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def __str__(self):
        return "Name: {}\tSurname: {}\tBirth: {}".format(self.name, self.surname, self.birth_date)

    def how_old(self, date):
        date_arr = date.split("/")
        arr_date = self.birth_date.split("/")
        return int(date_arr[0]) - int(arr_date[0]) if (int(date_arr[1]) < int(arr_date[1])) else int(date_arr[0]) - int(arr_date[0])

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def surname(self):
        return self._surname
    @surname.setter
    def surname(self, value):
        self._surname = value
    @property
    def birth_date(self):
        return self._birth_date
    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

class BankAccount:
    def __init__(self, account_number, money):
        self.account_number = account_number
        self.money = money

    def __str__(self):
        return "Account Number: {}\tMoney: {}".format(self.account_number, self.money)

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value

    def add_money(self, value):
        self.money += value

    def get_money(self, value):
        if value < self.money:
            self.money -= value
        else:
            print("you haven't got this much money")

    def show_money(self):
        return self.money

class Client(Citizen, BankAccount):
    def __init__(self, name, surname, birth_date, account_number, money):
        Citizen.__init__(self, name, surname, birth_date)
        BankAccount.__init__(self, account_number, money)

    def __str__(self):
        return super().__str__()

class VipClient(Client):
    p = 20

    def __init__(self, name, surname, birth_date, account_number, money, last_credit_date, current_credit_sum, remaining):
        super().__init__(name, surname, birth_date, account_number, money)
        self.last_credit_date = last_credit_date
        self.current_credit_sum = current_credit_sum
        self.remaining = remaining

    def __str__(self):
        return super().__str__() + "\tlast_credit_date: {}\tcurrent_credit_sum: {}\tremaining_money: {}".format(self.last_credit_date, self.current_credit_sum, self.remaining)


    def earn_credit(self):
        if self.how_old("2022/10/7") in range(30, 51):
            self.remaining += (self.money*self.p)/100
        else:
            self.remaining += (self.money*self.p)/200

    def return_credit(self):
        if self.current_credit_sum > self.current_credit_sum:
            self.money -= self.current_credit_sum - self.remaining
            self.credit_money = 0
            self.credit_sum = 0
        else:
            self.credit_money -= self.credit_sum
            self.credit_sum = 0

    @property
    def last_credit_date(self):
        return self._last_credit_date

    @last_credit_date.setter
    def last_credit_date(self, value):
        self._last_credit_date = value

    @property
    def current_credit_sum(self):
        return self._current_credit_sum

    @current_credit_sum.setter
    def current_credit_sum(self, value):
        self._current_credit_sum = value

    @property
    def remaining(self):
        return self._remaining

    @remaining.setter
    def remaining(self, value):
        self._remaining = value

np = VipClient("Nazarii", "Protskiv", "2003/12/29", "5326532598654125", 120, "2021/7/8", 100, 20)
sh = VipClient("Sofiia", "Hoshko", "2005/12/7", "5326532598634265", 120, "2020/5/7", 500, 20)
gd = VipClient("Dmytro", "Granovskiy", "2004/6/10", "53265325983545625", 900, "2019/2/1", 100, 20)
vt = Client("Volodymyr", "Tutko", "2003/10/20", "5326532598634525", 100)
zo = Client("Zhenchenko", "Oleksandr", "2003/12/28", "53234678654125", 150)


clients = [np, sh, gd, vt, zo]
sorted_cl = sorted(clients, key=lambda x: x.surname)

for i in sorted_cl:
    print(i)

clients_with_credits = [i for i in clients if type(i) == VipClient and i.last_credit_date != ""]
for i in clients_with_credits:
    print(i)
