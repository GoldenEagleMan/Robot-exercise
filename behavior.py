from abc import abstractclassmethod
from plab.sensob import *


class Behavior:
    def __init__(self, BBCON, sensobs, priority):
        self.BBCON = BBCON
        self.sensobs = sensobs
        self.motor_recommendations = None
        self.active_flag = False
        self.halt_request = False
        # halt request not yet implemented
        self.priority = priority
        self.match_degree = None
        self.weight = None
        self.name = ""

    @abstractclassmethod
    def consider_deactivation(self):
        # when active, consider if the behavior should be deactivated
        return

    @abstractclassmethod
    def consider_activation(self):
        # when deactivated, consider if the behavior should be activated
        return

    @abstractclassmethod
    def update(self):
        # update activity status
        # call sense_an_act
        # update behavior weight
        return

    @abstractclassmethod
    def sense_and_act(self):
        # produce motor recommendations based upon sensob readings
        return


'''The following behaviors should be implemented:

        - Follow line
        - Collision detection
        - Go around object
        - Endpoint detection
        - Red detector
        '''


# Collision detection behavior will avoid obstacles by driving around them
# WILL SPLIT COLLISION DETECTION INTO 2 SEPARATE ONES: 1 WILL STEER AWAY FROM AN OBJECT
# NAMED COLLISION DETECTION, THE OTHER ONE WILL GO AROUND THE OBJECT USING THE IR-SENSORS
# REMEMBER TO REMOVE IR-SENSOBS FROM THIS CLASS
class CollisionDetection(Behavior):
    def __init__(self, BBCON, sensobs, priority):
        super(CollisionDetection, self).__init__(BBCON, sensobs, priority)
        self.name = "Collision detection"
        self.u_sensob = Ultrasonic()
        self.l_IR_sensob = IRSensobLeft()
        self.r.IR_sensob = IRSensobRight()
        self.distance = 50  # 50mm
        self.sensobs.append(self.u_sensob)
        self.sensobs.append(self.l_IR_sensob)
        self.sensobs.append(self.r_IR_sensob)

    def consider_activation(self):
        # Collision detection will be/remain activated, if an object is close,
        # and whilst going around an object
        if self.u_sensob.get_value() < self.distance:
            self.active_flag = True
            self.halt_request = True

    def consider_deactivation(self):
        # Collision detection will be/remain deactivated, if there is no object spotted through ultrasound
        if (self.u_sensob.get_value() > self.distance):  # the preferred distance will be calculated later
            self.BBCON.deactivate_behavior(self)
            self.active_flag = False
            self.halt_request = False

    def update(self):
        for sensor in self.sensobs:
            sensor.update()

        if self.active_flag:
            self.consider_deactivation()

        elif not self.active_flag:
            self.consider_activation()

        if not self.active_flag:
            self.weight = 0
            return

        self.sense_and_act()
        self.weight = self.priority * self.match_degree

    def sense_and_act(self):
        self.motor_recommendations["turn left"]  # yet to be made, but will either pass the object on the left or right
        self.priority = 1
        self.match_degree = 1


# Go around object will be activated when collision detection has steered away from an object
# Go around object will go around an object such that its final destination will be on the other side of the object
class GoAroundObject(Behavior):
    def __init__(self, BBCON, sensobs, priority):
        super(GoAroundObject, self).__init__(BBCON, sensobs, priority)
        self.name = "Go around object"
        self.l_IR_sensob = IRSensobLeft()
        self.r.IR_sensob = IRSensobRight()
        self.sensobs.append(self.l_IR_sensob)
        self.sensobs.append(self.r_IR_sensob)

    def consider_activation(self):
        if (self.l_IR_sensob.get_value() or self.r_IR_sensob.get_value()):
            self.active_flag = True
            self.halt_request = True

    def consider_deactivation(self):
        if not (self.l_IR_sensob.get_value() or self.r_IR_sensob.get_value()):
            self.active_flag = True
            self.halt_request = True

    def update(self):
        if self.active:

    def sense_and_act(self):
#hello you sexy