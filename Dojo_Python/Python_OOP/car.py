class Car(object):
    def __init__ (self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print "Price: $" + str(self.price)
        print "Speed: ", self.speed
        print "Fuel: ", self.fuel
        print "Milage: ", self.mileage
        print "Tax: ", self.tax
        return self

car1 = Car(2000, '35 mph', 'Full', '60 mpg')
car2 = Car(200, '5 mph', 'Not full', '15 mpg')
car3 = Car(200000, '300 mph', 'Full', '120 mpg')
car4 = Car(15000, '120 mph', 'Kind of full', '35 mpg')
car5 = Car(9000, '90 mph', 'Empty', '20 mpg')
car6 = Car(1300, '75 mph', 'Not full', '65 mpg')

car1.display_all()
car2.display_all()
car3.display_all()
