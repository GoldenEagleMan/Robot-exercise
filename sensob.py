from plab.ultrasonic import *
from plab.reflectance_sensors import *
from plab.irproximity_sensor import *
from plab.camera import *

class Sensob:

    def __init__(self, sensors):
        self.value = None
        self.sensor = sensors  #1 sensor or list of used sensors

    def update(self):
        pass

    def reset(self):
        self.sensor.reset()
        pass

    def get_value(self):
        return self.value


class IRSensob(Sensob):

    def __init__(self):
        ir_sensor = IRProximitySensor()
        super().__init__(ir_sensor)


class ReflectanceBoardSensob(Sensob):

    def __init__(self):
        reflectance_board = ReflectanceSensors()
        super().__init__(reflectance_board)


class UltrasoundSensob(Sensob):

    def __init__(self):
        ultra = Ultrasonic()
        super().__init__(ultra)

    def update(self):
        self.value = int(self.sensor.get_value() * 10) #cm to mm


class LineFollowingSensob(ReflectanceBoardSensob):

    def __init__(self):
        super().__init__()

    def update(self):
        red_values = self.sensor.get_value()
        values_and_sensors = {}
        for i in range(0, len(red_values)):
            values_and_sensors[red_values[i]] = i
        red_values.sort(reverse=True)
        self.value = (values_and_sensors.get(red_values[0]), values_and_sensors.get(red_values[3]))


class EndpointDetectionSensob(ReflectanceBoardSensob):

    def __init__(self):
        super().__init__()

    def update(self):
        red_values = self.sensor.get_value()
        for value in red_values:
            if value - 0.05 > 0:
                self.value = False
        self.value = True


class IRSensobLeft(IRSensob):

    def __init__(self):
        super().__init__()

    def update(self):
        self.value = self.sensor.get_value()[0] #0,1 left and right? right and left?


class IRSensobRight(IRSensob):

    def __init__(self):
        super().__init__()

    def update(self):
        self.value = self.sensor.get_value()[1]


class CameraSensob(Sensob):

    def __init__(self):
        camera = Camera(128, 30)
        self.match_degree = 0
        super(CameraSensob, self).__init__(camera)

    def update(self):
        self.sensor.reset
        self.value = self.interpret_image()

    def interpret_image(self):
        camera = self.sensor
        camera.update()
        image = camera.value # the matrix of pixels
        occurrence_array = [0 for i in range(128)]

        for h in range(camera.img_height):
            for w in range(camera.img_width):
                pixel = image.getpixel(w,h)
                r, g, b = pixel[0], pixel[1], pixel[2]
                if r >= 180 and g < 45 and b < 45:
                    occurrence_array[w] += 1

        return (CameraSensob.max_index(occurrence_array) - camera.img_width)/camera.img_width #returns a value between -1 and 1

    @staticmethod
    def max_index(list):
        highest_index = 0
        for i in range(1, len(list)):
            if list[i] > list[highest_index]:
                highest_index = i
        return highest_index






