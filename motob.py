from motors import *


class Motob:

    def __init__(self):
        self.motors = Motors()
        self.value = None

    def update(self, motor_recommendation):
        self.value = motor_recommendation
        self.operationalize()

    def operationalize(self):
        command = self.value[0]
        angle = self.value[1]
        speed = 0.25 + 0.75 * abs(angle/90)

        print("Decoding motor recommendation...")
        print("Speed is " + str(speed))

        if command == "goForward":
            self.motors.set_value([speed, speed])
        elif command == "turn":
            print("turning")
            if angle > 0:
                self.motors.set_value([0.25, speed])
            else:
                self.motors.set_value([speed, 0.25])
        elif command == "goBackward":
            self.motors.set_value([- speed, - speed])
        elif command == "stopAllMotors":
            self.motors.stop()
        else:
            print("Unable to decode command")
