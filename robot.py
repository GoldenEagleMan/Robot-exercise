from BBCON import BBCON
from behavior import *
from sensob import *
from motob import Motob
from arbitrator import Arbitrator


class Robot:

    def __init__(self):
        arbitrator = Arbitrator(self)
        motob = Motob()
        self.controller = BBCON(Robot.build_behavior_list(), Robot.build_sensob_list(), motob, arbitrator)

    def run(self):
        run = True
        while run:
            run = self.controller.run_one_timestep()

    @staticmethod
    def build_sensob_list():
        cameraSensob = CameraSensob()
        irSensobRight = IRSensobRight()
        irSensobLeft = IRSensobLeft()
        endpointDetectionSensob = EndpointDetectionSensob()
        lineDetectionSensob = LineDetectionSensob()
        lineFollowingSensob = LineFollowingSensob()
        ultrasoundSensob = UltrasoundSensob()

        return [cameraSensob, irSensobRight, irSensobLeft, endpointDetectionSensob, lineDetectionSensob,
                   lineFollowingSensob, ultrasoundSensob]
    @staticmethod
    def build_behavior_list():
        collisionDetectionBehavior = CollisionDetection()
        goAroundObjectBehavior = GoAroundObject()
        followLineBehavior = FollowLine()
        redDetectorBehavior = RedDetector()

        return [collisionDetectionBehavior, goAroundObjectBehavior, followLineBehavior, redDetectorBehavior]
