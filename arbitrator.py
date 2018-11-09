class Arbitrator:
    def __init__(self):
        self.bbcon = None

    def choose_action(self):
        #active_behaviors = filter(lambda x: x.active_flag == True, self.bbcon.behaviors)
        prioritized_behavior = None
        for behavior in self.bbcon.active_behaviors:
            if prioritized_behavior is None or prioritized_behavior.weight < behavior.weight:
                prioritized_behavior = behavior
        self.bbcon.run_behavior = (prioritized_behavior.motor_recommendations, prioritized_behavior.halt_request)