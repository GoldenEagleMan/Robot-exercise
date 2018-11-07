class BBCON:
#hallobois spam
    def __init__(self, behaviors, sensobs, motobs, arbitrator):
        self.behaviors = behaviors
        self.sensobs = sensobs
        self.motobs = motobs
        self.active_behaviors = []
        self.active_sensobs = []
        self.arbitrator = arbitrator
        self.run_behavior = None

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)
        pass

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)
        pass

    def activate_behavior(self, behavior):
        behavior.active_flag = True
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)
        for sensob in behavior.sensobs:
            if sensob not in self.active_sensobs:
                self.active_sensobs.append(sensob)
        pass

    def deactivate_behavior(self, behavior):
        behavior.active_flag = False
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)
        for sensob in behavior.sensobs:
            if sensob in self.active_sensobs:
                self.active_sensobs.remove(sensob)

        pass

    def run_one_timestep(self):
        #update all sensob
        for sensob in self.active_sensobs:
            sensob.update()
        #update all behaviors
        for behavior in self.behaviors:
            behavior.update()
        #invoke arbitrator.
        self.arbitrator.choose_action() #can be it must be passed a list of behaviors
        #update all motors
        if self.run_behavior[1] != False:
            self.motobs.decodeMR(self.run_behavior[0])
        else:
            self.end_program()
            #Wait

        #reset all sensob

        for sensob in self.active_sensobs:
            sensob.reset()

    def end_program(self):
        pass