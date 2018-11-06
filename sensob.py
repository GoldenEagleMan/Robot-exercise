from plab.ultrasonic import *
from plab.reflectance_sensors import *

class Sensob:

    def __init__(self, sensors):
        self.value = None
        self.sensors = sensors #1 sensor or list of used sensors

    def update(self):
        for sensor in self.sensors:
            sensor.reset()
            sensor.update

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()
            pass
        

class LineFollowingSensob(Sensob):
    
    def __init__(self):
        reflectance_board = ReflectanceSensors()
        super(LineFollowingSensob, self).__init__(reflectance_board)

    def update(self):
        super().update()
        red_values = self.sensors.get_value()
        values_and_sensors = {}
        for i in range(0, len(red_values)):
            values_and_sensors[red_values[i]] = i
        red_values.sort(reverse=True)
        self.value = (values_and_sensors.get(red_values[0]), values_and_sensors.get(red_values[3]))



