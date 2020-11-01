class Car:
    def __init__(self, color, speed, gear):
        self.color = color
        self.speed = speed
        self.gear = gear

    def toString(cls):
        print('색상\t속도\t기어')
