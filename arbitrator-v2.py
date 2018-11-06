class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        prioritized_behavior = None
        for behavior in self.bbcon.behaviors:
            if prioritized_behavior == None or prioritized_behavior.weigth < behavior.weigth:
                prioritized_behavior = behavior
        return (prioritized_behavior.motor_recommendations, prioritized_behavior.halt_request)
