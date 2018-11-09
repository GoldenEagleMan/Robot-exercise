from BBCON import BBCON
from behavior import *
from sensob import *
from motob import Motob
from arbitrator import Arbitrator


class Robot:

    def __init__(self):
        self.arbitrator = Arbitrator()
        motob = Motob()
        self.sensobs = None
        self.behaviors = None
        self.controller = BBCON(motob, self.arbitrator)
        self.arbitrator.bbcon = self.controller
        self.build_sensob_and_behavior_list()
        self.connect_behaviors_and_sensobs_to_controller()

    def run(self):
        run = True
        while run:
            run = self.controller.run_one_timestep()

    def connect_behaviors_and_sensobs_to_controller(self):
        for sensob in self.sensobs:
            self.controller.sensobs.append(sensob)
        for behavior in self.behaviors:
            self.controller.behaviors.append(behavior)
        pass

    def build_sensob_and_behavior_list(self):
        cameraSensob = CameraSensob()
        irSensobRight = IRSensobRight()
        irSensobLeft = IRSensobLeft()
        endpointDetectionSensob = EndpointDetectionSensob()
        lineDetectionSensob = LineDetectionSensob()
        lineFollowingSensob = LineFollowingSensob()
        ultrasoundSensob = UltrasoundSensob()

        self.sensobs = [cameraSensob, irSensobRight, irSensobLeft, endpointDetectionSensob, lineDetectionSensob,
                   lineFollowingSensob, ultrasoundSensob]

        collisionDetectionBehavior = CollisionDetection(self.controller, [ultrasoundSensob], 1)
        goAroundObjectBehavior = GoAroundObject(self.controller, [irSensobLeft, irSensobRight], 1)
        followLineBehavior = FollowLine(self.controller, [lineFollowingSensob, endpointDetectionSensob, lineDetectionSensob], 1)
        redDetectorBehavior = RedDetector(self.controller, [cameraSensob], 1)

        self.behaviors = [collisionDetectionBehavior, goAroundObjectBehavior, followLineBehavior, redDetectorBehavior]

