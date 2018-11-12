from sensob import CameraSensob
from motob import Motob
from arbitrator import Arbitrator
from behavior import *
from sensob import *
from zumo_button import *
from ultrasonic import *
from reflectance_sensors import *
from irproximity_sensor import *

class BBCON:

    def __init__(self):
        self.motob = Motob()
        self.sensors = None
        self.behaviors = None
        self.sensobs = None
        self.build_sensob_and_behavior_list()
        self.compile_active_behavior_list()
        self.active_behaviors = []
        self.arbitrator = Arbitrator(self)
        self.run_behavior = (["forward", 0], False)
        #self.run_behavior = ('F',0.5 )



    def run_one_timestep(self):
        self.compile_active_behavior_list()
        print("updating objects")
        self.update_objects()
        #invoke arbitrator.
        print("choosing action")
        self.arbitrator.choose_action()
        self.print_info_to_console()
      #  if self.run_behavior[1]:
       #     self.end_program()
        self.motob.update(self.run_behavior)
        #reset all sensob
        '''for sensob in self.active_sensobs:
            sensob.reset()'''
        return True

    def activate_behavior(self, behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)
        pass

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)
        pass


    def compile_active_behavior_list(self):

        # construct active behaviors list
        self.active_behaviors = []
        for behavior in self.behaviors:
            if behavior.active_flag:
                self.active_behaviors.append(behavior)


    def update_objects(self):
        #update all sensors, sensobs and behaviors
        camera_sensob = None
        print("updating sensors")
        for sensor in self.sensors:
            print("Updating " + sensor.__class__.__name__)
            sensor.update()
        print("updating Sensobs")
        for sensob in self.sensobs:
            if not isinstance(sensob, CameraSensob):
                sensob.update()
            else:
                camera_sensob = sensob
        if self.behaviors[3].active_flag:
            print("updating camera")
            camera_sensob.update()
        print("updating behaviors")
        for behavior in self.behaviors:
            behavior.update()

    def end_program(self):
        self.motob.update(("stopAllMotors", 0))
        return False


    def print_info_to_console(self):
        print("****************************************************")
        print("**************** Sensors Values ********************")
        for sensor in self.sensors:
            print(sensor.__class__.__name__ + ": " + str(sensor.get_value()))
        print("**************** Sensobs Values ********************")
        for sensob in self.sensobs:
            print(sensob.__class__.__name__ + ": " + str(sensob.get_value()))
        print("*************** Active Behaviors *******************")
        for behavior in self.active_behaviors:
            print(behavior.__class__.__name__ + ": " + str(behavior.weight))
        print("************ Active recommendation *****************")
        print(self.run_behavior)
        print("****************************************************")
        print("****************************************************")



    def build_sensob_and_behavior_list(self):
        ir_proximity_sensor = IRProximitySensor()
        reflectance_board = ReflectanceSensors()
        ultrasonic_sensor = Ultrasonic()
        camera = Camera(128, 30)

        self.sensors = [ir_proximity_sensor, reflectance_board, ultrasonic_sensor]

        camera_sensob = CameraSensob(camera)
        ir_sensob_right = IRSensobRight(ir_proximity_sensor)
        ir_sensob_left = IRSensobLeft(ir_proximity_sensor)
        endpoint_detection_sensob = EndpointDetectionSensob(reflectance_board)
        line_detection_sensob = LineDetectionSensob(reflectance_board)
        line_following_sensob = LineFollowingSensob(reflectance_board)
        ultrasound_sensob = UltrasoundSensob(ultrasonic_sensor)

        self.sensobs = [camera_sensob, ir_sensob_right, ir_sensob_left, endpoint_detection_sensob, line_detection_sensob,
                   line_following_sensob, ultrasound_sensob]

        collision_detection_behavior = CollisionDetection(self, [ultrasound_sensob], 1)
        go_around_object_behavior = GoAroundObject(self, [ir_sensob_left, ir_sensob_right], 1)
        follow_line_behavior = FollowLine(self, [line_following_sensob, endpoint_detection_sensob, line_detection_sensob], 1)
        red_detector_behavior = RedDetector(self, [camera_sensob, endpoint_detection_sensob], 1)

        self.behaviors = [collision_detection_behavior, go_around_object_behavior, follow_line_behavior, red_detector_behavior]
        print("Sensors, Sensobs and Behaviors generated!")



    def run(self):
        run = True
        while run:
            run = self.run_one_timestep()

if __name__ == "__main__":
    bbcon = BBCON()
    print("Press the button to start the robot")
    ZumoButton().wait_for_press()
    while True:
        bbcon.run_one_timestep()
