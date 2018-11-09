from plab.motors import *


class Motob:

    def __init__(self):
        motors = Motors()
        self.motors = motors

    def decodeMR(self, motor_recommendation): #in form ("command", angle)
        command = motor_recommendation[0]
        angle = motor_recommendation[1]
        if command == "goForward":
            self.motors.forward(self.angle_to_speed(angle), 3)
        elif command == "turn":
            if angle > 0:
                self.motors.right(self.angle_to_speed(angle), 3)
            else:
                self.motors.left(self.angle_to_speed(angle), 3)
        elif command == "goBackward":
            self.motors.backward(self.angle_to_speed(angle), 3)
        elif command == "stopAllMotors":
            self.motors.stop()
        pass

    @staticmethod
    def angle_to_speed(angle):
        default_speed = 0.25
        return default_speed + (1 - default_speed) * abs(angle / 90)
