class Bike(object):
    def __init__(self, price, max_speed):
        # print "New bike!!!" # make sure init is working; will print for each new instance created
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Price: $", self.price, "; maximum speed: ", self.max_speed, "; total miles: ", self.miles
        return self

    def ride(self):
        print 'riding...'
        self.miles += 10
        return self

    def reverse(self):
        print 'reversing...'
        # if self.miles <= 0:
        #     print "You've gone into the negative miles! Try moving forward for a while..."
        #     return self
        if self.miles > 5:
            self.miles -= 5
        return self

bike1 = Bike(200, '25 mph')
bike2 = Bike(600, '55 mph')
bike3 = Bike(20, '5 mph')

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
