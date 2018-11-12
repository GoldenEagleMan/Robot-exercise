from sensob import CameraSensob

class BBCON:
#hallobois spam
    def __init__(self, motobs, arbitrator):
        self.behaviors = []
        self.sensobs = []
        self.motobs = motobs
        self.active_behaviors = []
        self.active_sensobs = []
        self.active_sensors = []
        self.arbitrator = arbitrator
        self.run_behavior = None
        self.sensors = []


    def run_one_timestep(self):
        self.compile_objects_list()
        self.update_objects()
        #invoke arbitrator.
        self.arbitrator.choose_action()
        self.print_info_to_console()
        if self.run_behavior[1]:
            self.end_program()
        self.motobs.decodeMR(self.run_behavior[0])
        #reset all sensob
        for sensob in self.active_sensobs:
            sensob.reset()
        return True
    def construct_sensors(self):
        for sensob in self.sensobs:
            self.activate_sensor(sensob.sensor)

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)
        pass

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)
        pass

    def activate_behavior(self, behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)
        pass

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)
        pass

    def activate_sensob(self, sensob):
        if sensob not in self.active_sensobs:
            self.active_sensobs.append(sensob)

    def activate_sensor(self, sensor):
        if sensor not in self.active_sensors:
            self.sensors.append(sensor)

    def compile_objects_list(self):

        # construct active behaviors list
        self.active_behaviors = []
        for behavior in self.behaviors:
            if behavior.active_flag:
                self.active_behaviors.append(behavior)
                '''
        # construct active sensobs list
        self.active_sensobs = []
        for behavior in self.active_behaviors:
            for sensob in behavior.sensobs:
                self.activate_sensob(sensob)

        # construct active sensor list
        self.active_sensors = []
        for sensob in self.active_sensobs:
            self.activate_sensor(sensob.sensor)
'''
    def update_objects(self):
        #update all sensors, sensobs and behaviors
        camera_sensob = None
        for sensor in self.sensors:
            sensor.reset()
            sensor.update()
        for sensob in self.sensobs:
            if not isinstance(sensob, CameraSensob):
                sensob.update()
            else:
                camera_sensob = sensob
        if self.behaviors[3].active_flag:
            camera_sensob.update()
        for behavior in self.behaviors:
            behavior.update()

    def end_program(self):
        self.motobs.decodeMR(("stopAllMotors", 0))
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


