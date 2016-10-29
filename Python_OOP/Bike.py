class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Price: $ ", self.price
        print "Max speed: ", self.max_speed, "mph"
        print "Total miles: ", self.miles

    def ride(self):
        print "Riding..."
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        return self

Andrew = Bike(100, 9000)
Andrew.ride().ride().ride().reverse().displayInfo()

Yo = Bike(2000, 500)
Yo.ride().ride().reverse().reverse().displayInfo()
