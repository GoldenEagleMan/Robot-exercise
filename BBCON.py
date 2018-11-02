class BBCON:

    def __init__(self, behaviors, sensobs, motobs, arbitrator):
        self.behaviors = behaviors
        self.sensobs = sensobs
        self.motobs = motobs
        self.active_behaviors = None
        self.arbitrator = arbitrator
        self.arbitrator.BBCON = self

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

    def run_one_timestep(self):
        #update all sensob
        for sensob in self.sensobs:
            sensob.update()
        #update all behaviors
        for behavior in self.behaviors:
            behavior.update()
        #invoke arbitrar.
        self.arbitrator.choose_action() #can be it must be passed a list of behaviors
        #update all motors
            #not yet implemed
        #Wait
            # not yet implemed
        #reset all sensob
        for sensob in self.sensobs:
            sensob.reset()

