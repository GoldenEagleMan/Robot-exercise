class Behavior:

    def __init__(self, BBCON, sensobs, priority):
        self.BBCON = BBCON
        self.sensobs = sensobs
        self.motor_recommendations = None
        self.active_flag = False
        #halt request not yet implemented
        self.priority = priority
        self.match_degree = None
        self.weight = None

    
