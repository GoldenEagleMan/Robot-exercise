from robot_test_files.motor_object import *
from random import randint

class MotorController():
    def __init__(self):
        self.motor_object = MotorObject()
        self.actions = ["goForward","goRight", "goLeft", "goBackward"]

    def run(self):
        while True:
            self.motor_object.drive(self.actions[randint(0, 3)])
