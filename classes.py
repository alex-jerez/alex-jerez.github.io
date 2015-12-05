class TransportationVehicle(object):
     def __init__(self):
        self.wheels = None
        self.color = None
        self.brand = None

class Car(TransportationVehicle):
    def __init__(self, color, year, make):
        self.color = color
        self.year = year
        self.make = make

    def __repr__(self):
        return "this car is a %s %s %s" % (self.color,
                self.year,
                self.make)

    def about(self):
        print "this car is a %s %s %s" % (self.color,
                self.year,
                self.make)
    @staticmethod
    def honk():
        print "HONK!"

    @classmethod
    def honkAndSay(cls, word):
        cls.honk()
        print word
