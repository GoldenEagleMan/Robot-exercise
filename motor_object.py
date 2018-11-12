from plab.motors import *


class MotorObject():
    def __init__(self):
        motors = Motors()
        self.motors = motors

    def drive(self, command):
        if command == "goForward":
            self.motors.forward(0.5,1)
        elif command == "turnRight":
            self.motors.right(0.5,1)
        elif command == "turnLeft":
            self.motors.left(0.5,1)
        elif command == "goBackward":
            self.motors.backward(0.5,1)
        elif command == "stopAllMotors":
            self.motors.stop()
