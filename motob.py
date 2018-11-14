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
        speed = 0.10 + 0.90 * abs(angle/90)
        time = 1
        if command == "goForward":
            self.motor.set_value((speed*1.5, speed*1.5))
            #self.motor.forward(speed)
        elif command == "turn":
            if angle > 0:
                self.motor.set_value((speed, -speed/2))
                #self.motor.left(speed)
            else:
                self.motor.set_value((-speed/2, speed))
                #self.motor.right(speed)
        elif command == "turnAndWait":
            if angle > 0:
                self.motor.set_value((speed, -speed / 2, time))
                # self.motor.left(speed)
            else:
                self.motor.set_value((-speed / 2, speed, time))
                # self.motor.right(speed)
        elif command == "goBackward":
            self.motor.set_value((- speed, - speed))
            #self.motor.backward(speed)
        elif command == "stopAllMotors":
            self.motor.stop()
        else:
            print("Unable to decode command")
        self.print_info_to_console(speed, command, time)

    def print_info_to_console(self, speed, direction, wait):
        print("********************Motors info*********************")
        print("Performing " + str(direction) + " with speed " + str(speed) +" for " +str(wait) +"s")
        print("********************end*****************************")
        print("****************************************************")

