from motors import Motors


class Motob:

    def __init__(self):
        self.motor = Motors()
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
        print(self.value)
        if command == "goForward":
            self.motor.set_value((speed, speed))
            #self.motor.forward(speed)
        elif command == "turn":
            print("turning")
            if angle > 0:
                self.motor.set_value((0.25, speed))
                #self.motor.left(speed)
            else:
                self.motor.set_value((speed, 0.25))
                #self.motor.right(speed)
        elif command == "goBackward":
            self.motor.set_value((- speed, - speed))
            #self.motor.backward(speed)
        elif command == "stopAllMotors":
            self.motor.stop()
        else:
            print("Unable to decode command")
        pass