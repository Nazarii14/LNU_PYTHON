class Ware:
    p = 20

    def __init__(self, id, date, price):
        self.id = id
        self.date = date
        self.price = price

    def __str__(self):
        return "ID: {}\tDATE: {}\tPRICE: {}".format(self.id, self.date, self.price)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        self._date = value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value


class Computer(Ware):
    def __init__(self, id, date, price, mark, processor_speed, ram_size, drive_size):
        super().__init__(id, date, price)
        self.mark = mark
        self.processor_speed = processor_speed
        self.ram_size = ram_size
        self.drive_size = drive_size

    def __str__(self):
        return super().__str__() + "\tMARK: {}\tProcessor Speed: {}\tRAM: {}\tDrive: {}".format(self.mark, self.processor_speed, self.ram_size, self.drive_size)

    @property
    def mark(self):
        return self._mark
    @mark.setter
    def mark(self, value):
        self._mark = value
    @property
    def processor_speed(self):
        return self._processor_speed
    @processor_speed.setter
    def processor_speed(self, value):
        self._processor_speed = value
    @property
    def ram_size(self):
        return self._ram_size
    @ram_size.setter
    def ram_size(self, value):
        self._ram_size = value
    @property
    def drive_size(self):
        return self._drive_size
    @drive_size.setter
    def drive_size(self, value):
        self._drive_size = value

class Server(Computer):
    def __init__(self, id, date, price, mark, processor_speed, ram_size, drive_size, extra_drive):
        super().__init__(id, date, price, mark, processor_speed, ram_size, drive_size)
        self.extra_drive = extra_drive

    def __str__(self):
        return super().__str__() + "\tExtra Drive: {}".format(self.extra_drive)

    @property
    def extra_drive(self):
        return self._extra_drive
    @extra_drive.setter
    def extra_drive(self, value):
        self._extra_drive = value


class WorkStation(Computer):
    def __init__(self, id, date, price, mark, processor_speed, ram_size, drive_size, diagonal_size):
        super().__init__(id, date, price, mark, processor_speed, ram_size, drive_size)
        self.diagonal_size = diagonal_size

    def __str__(self):
        return super().__str__() + "    Diagonal size: {}".format(self.diagonal_size)

    @property
    def diagonal_size(self):
        return self._diagonal_size
    @diagonal_size.setter
    def diagonal_size(self, value):
        self._diagonal_size = value


class Notebook(Computer):
    def __init__(self, id, date, price, mark, processor_speed, ram_size, drive_size, diagonal_size, weight):
        super().__init__(id, date, price, mark, processor_speed, ram_size, drive_size)
        self.diagonal_size = diagonal_size
        self.weight = weight

    def __str__(self):
        return super().__str__() + "    Diagonal size: {}    Weight: {}".format(self.diagonal_size, self.weight)

    @property
    def diagonal_size(self):
        return self._diagonal_size
    @diagonal_size.setter
    def diagonal_size(self, value):
        self._diagonal_size = value
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, value):
        self._weight = value


class HardWare:
    print("prodav")


serv1 = Server(15, 2020, 21000, "Apple", 1000, 8, 512, 1024)
serv2 = Server(20, 2015, 13000, "Samsung", 600, 6, 256, 1024)
serv3 = Server(17, 2022, 20000, "SuperGT", 2500, 16, 256, 2048)
wk1 = WorkStation(23, 2019, 12000, "Builder", 500, 9, 800, 17)
wk2 = WorkStation(22, 2011, 10500, "Builder1", 750, 2, 850, 21)
nt1 = Notebook(0, 2017, 16000, "Samsung", 1000, 8, 1200, 540, 0.6)
nt2 = Notebook(5, 2019, 20000, "Infernus", 2000, 16, 2300, 1200, 3.1)
nt3 = Notebook(78, 2021, 18000, "Samsung", 1300, 12, 1600, 746, 2.3)

products = [serv1, serv2, serv3, wk1, wk2, nt1, nt2, nt3]
for i in products:
    print(i)

print()
ids = [15, 17, 23, 78]
for i in products:
    if i.id in ids:
        print(i)


print("\nServers:")
servers = sorted([i for i in products if type(i) == Server], key=lambda x: -x.date)
for i in servers:
    print(i)

print("\nNotebooks:")
notebooks = sorted([i for i in products if type(i) == Notebook], key=lambda x: -x.date)
for i in notebooks:
    print(i)

print("\nWorkstations:")
workstations = sorted([i for i in products if type(i) == WorkStation], key=lambda x: -x.date)
for i in workstations:
    print(i)

