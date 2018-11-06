from plab.ultrasonic import *
from plab.reflectance_sensors import *

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
        

class IR_Array_Sensob(Sensob):
    
    def __init__(self):
        reflectance_board = ReflectanceSensors()
        super(IR_Array_Sensob, self).__init__([reflectance_board])

    def update(self):
        super().update()
        