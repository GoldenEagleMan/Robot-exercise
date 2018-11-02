from plab.ultrasonic import *


class Sensob:

    def __init__(self, sensors):
        self.data = None
        self.sensors = sensors

    def update(self):
        for sensor in self.sensors:
            sensor.reset()
            sensor.update()
            sensor.get_value()

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()
            pass