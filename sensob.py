from ultrasonic import *
from reflectance_sensors import *
from irproximity_sensor import *
from camera import *

class Sensob:

    def __init__(self, sensor):
        self.value = None
        self.sensor = sensor #1 sensor or list of used sensors

    def update(self):
        pass

    def reset(self):
        self.sensor.reset()
        pass

    def get_value(self):
        return self.value


class UltrasoundSensob(Sensob):

    def update(self):
        self.value = int(self.sensor.get_value() * 10) #cm to mm


class LineFollowingSensob(Sensob):

    def update(self):
        red_values = self.sensor.get_value()
        values_and_sensors = {}
        for i in range(0, len(red_values)):
            values_and_sensors[red_values[i]] = i
        red_values.sort(reverse=True)
        self.value = values_and_sensors.get(red_values[0])


class LineDetectionSensob(Sensob):

    def update(self):
        red_values = self.sensor.get_value()
        for value in red_values:
            if value <= 0.1:
                self.value = True
        self.value = False


class EndpointDetectionSensob(Sensob):

    def update(self):
        red_values = self.sensor.get_value()
        treshold = 5
        for value in red_values:
            treshold -= value
        if treshold >= 2.5:
            self.value = True
        self.value = False


class IRSensobLeft(Sensob):

    def update(self):
        self.value = self.sensor.get_value()[0] #0,1 left and right? right and left?
        pass

class IRSensobRight(Sensob):

    def update(self):
        self.value = self.sensor.get_value()[1]
        pass

class CameraSensob(Sensob):

    def __init__(self, camera):
        self.match_degree = 0
        super().__init__(camera)

    def update(self):
        self.sensor.reset()
        self.value = self.interpret_image()
        '''
        value is a tuple consisting of a bool (whether the picture is red or not) and
        a number between -1 and 1 that represents the direction of the redness
        '''

    def interpret_image(self):
        camera = self.sensor
        camera.update()
        image = camera.value # the matrix of pixels
        occurrence_array = [0 for i in range(128)]
        pixel_counter = 0 # counts the amount of red pixels

        for h in range(camera.img_height):
            for w in range(camera.img_width):
                pixel = image.getpixel((w, h))
                r, g, b = pixel[0], pixel[1], pixel[2]
                if r >= 180 and g < 45 and b < 45:
                    occurrence_array[w] += 1
                    pixel_counter += 1

        direction = (CameraSensob.max_index(occurrence_array) - camera.img_width)/camera.img_width
        redness = pixel_counter/(camera.img_width*camera.img_height)
        threshold = 0.10  # how many percent of red pixels that is needed to be considered red
        if redness > threshold:
            return (True, direction)
        else:
            return (False, direction)


    @staticmethod
    def max_index(list):
        highest_index = 0
        for i in range(1, len(list)):
            if list[i] > list[highest_index]:
                highest_index = i
        return highest_index






