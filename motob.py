from plab.motors import *


class Motob:

    def __init__(self):
        motors = Motors()
        self.motors = motors

    def decodeMR(self, motor_recommendation): #in form ("command", angle)

        command = motor_recommendation[0]
        speed = Motob.angle_to_speed(motor_recommendation[1])
        angle = motor_recommendation[1]

        print("Decoding motor recommendation...")
        print("Speed is " + str(speed))

        if command == "goForward":
            self.motors.forward(speed, 4)
        elif command == "turn":
            print("turning")
            if angle > 0:
                self.motors.right(speed, 4)
            else:
                self.motors.left(speed, 4)
        elif command == "goBackward":
            self.motors.backward(speed, 4)
        elif command == "stopAllMotors":
            self.motors.stop()
        pass

    @staticmethod
    def angle_to_speed(angle):
        default_speed = 0.25
        return default_speed + (1 - default_speed) * abs(angle / 90)
