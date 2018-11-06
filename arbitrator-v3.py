class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        active_behaviors = filter(lambda x: x.active_flag == True, self.bbcon.behaviors)
        prioritized_behavior = None
        for behavior in active_behaviors:
            if prioritized_behavior == None or prioritized_behavior.weigth < behavior.weigth:
                prioritized_behavior = behavior
        return (prioritized_behavior.motor_recommendations, prioritized_behavior.halt_request)
