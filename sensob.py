from plab.ultrasonic import *
from plab.reflectance_sensors import *
from plab.irproximity_sensor import *


class Sensob:

    def __init__(self, sensors):
        self.value = None
        self.sensors = sensors  #1 sensor or list of used sensors

    def update(self):
        pass

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()
            pass


class IRSensob(Sensob):

    def __init__(self):
        ir_sensor = IRProximitySensor()
        super().__init__(ir_sensor)

    def update(self):
        self.sensors.reset()
        self.sensors.update()


class ReflectanceBoardSensob(Sensob):

    def __init__(self):
        reflectance_board = ReflectanceSensors()
        super().__init__(reflectance_board)

    def update(self):
        self.sensors.reset()
        self.sensors.update()


class UltrasoundSensob(Sensob):

    def __init__(self):
        ultra = Ultrasonic()
        super().__init__(ultra)

    def update(self):
        self.sensors.reset()
        self.sensors.update()


class LineFollowingSensob(ReflectanceBoardSensob):

    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        red_values = self.sensors.get_value()
        values_and_sensors = {}
        for i in range(0, len(red_values)):
            values_and_sensors[red_values[i]] = i
        red_values.sort(reverse=True)
        self.value = (values_and_sensors.get(red_values[0]), values_and_sensors.get(red_values[3]))


class EndpointDetectionSensob(ReflectanceBoardSensob):

    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        red_values = self.sensors.get_value()
        for value in red_values:
            if value - 0.05 > 0:
                self.value = False
        self.value = True


class IRSensobLeft(IRSensob):

    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        self.value = self.sensors.get_value()[0] #0,1 left and right? right and left?


class IRSensobRight(IRSensob):

    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        self.value = self.sensors.get_value()[1]







