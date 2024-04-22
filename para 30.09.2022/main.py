class Vehicle:

    def __init__(self, mark, power, num_of_wheels, weight):
        self.mark = mark
        self.power = power
        self.num_of_wheels = num_of_wheels
        self.weight = weight

    def __str__(self):
        return "Mark: {}   Power: {}   Number of wheels: {}   Weight {}".format(self.mark, self.power, self.num_of_wheels, self.weight)

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, mark):
        self._mark = mark

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    @property
    def num_of_wheels(self):
        return self._num_of_wheels

    @num_of_wheels.setter
    def num_of_wheels(self, value):
        self._num_of_wheels = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value



class Truck(Vehicle):
    def __init__(self, mark, power, num_of_wheels, weight, load_capacity):
        super().__init__(mark, power, num_of_wheels, weight)
        self.load_capacity = load_capacity

    @property
    def load_capacity(self):
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, value):
        self._load_capacity = value

    def __str__(self):
        return super().__str__() + "   Load capacity {}".format(self.load_capacity)


class Car(Vehicle):
    def __init__(self, mark, power, num_of_wheels, weight, num_of_seats):
        super().__init__(mark, power, num_of_wheels, weight)
        self.num_of_seats = num_of_seats

    @property
    def num_of_seats(self):
        return self._num_of_seats

    @num_of_seats.setter
    def num_of_seats(self, value):
        self._num_of_seats = value

    def __str__(self):
        return super().__str__() + "   num_of_seats: {}".format(self.num_of_seats)


class Bus(Vehicle):
    def __init__(self, mark, power, num_of_wheels, weight, num_of_seats, num_of_standing_places):
        super().__init__(mark, power, num_of_wheels, weight)
        self.num_of_seats = num_of_seats
        self.num_of_standing_places = num_of_standing_places

    @property
    def num_of_seats(self):
        return self._num_of_seats

    @num_of_seats.setter
    def num_of_seats(self, value):
        self._num_of_seats = value

    @property
    def num_of_standing_places(self):
        return self._num_of_standing_places

    @num_of_standing_places.setter
    def num_of_standing_places(self, value):
        self._num_of_standing_places = value

    def __str__(self):
        return super().__str__() + "    num_of_seats: {}   num_of_standing_places: {}".format(self.num_of_seats, self.num_of_standing_places)

v1 = Vehicle("BMW", 540, 4, 2000)
v2 = Vehicle("BMW", 600, 4, 1600)
t1 = Truck("Mercedes", 1100, 8, 2000, 777)
t2 = Truck("Mercedes", 1000, 8, 2000, 777)
c1 = Car("Smart", 100, 4, 700, 4)
c2 = Car("Volvo", 250, 4, 450, 4)
b1 = Bus("Mercedes", 500, 6, 1800, 40, 80)
b2 = Bus("Mercedes", 500, 6, 1800, 40, 80)

autopark = [v1, v2, t1, t2, c1, c2, b1, b2]

for i in autopark:
    print(i)


print()
print("Sorted by power:")
sorted_by_power = sorted(autopark, key=lambda x: x.power)
for i in sorted_by_power:
    print(i)


trucks = [x for x in autopark if type(x) == Truck]
cars = [x for x in autopark if type(x) == Car]


print()
for i in trucks:
    print(i)

print()
for i in cars:
    print(i)

