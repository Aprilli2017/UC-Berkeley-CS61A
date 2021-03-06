class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, model_type):
        self.wheels = Car.num_wheels
        self.color = 'No color yet. You need to paint me.'
        self.model = model_type
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return self.model + ' cannot drive!'
        self.gas -= 10
        return self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 30
        print('Your car is full.')


class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return Car.drive(self)


