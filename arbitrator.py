class Arbitrator:
    def __init__(self):
        self.bbcon = None

    def choose_action(self):
        #active_behaviors = filter(lambda x: x.active_flag == True, self.bbcon.behaviors)
        prioritized_behavior = None
        for behavior in self.bbcon.active_behaviors:
            print("weight of evalueting behavior is " + str(behavior.weight))
            if prioritized_behavior is None or prioritized_behavior.weight < behavior.weight:
                prioritized_behavior = behavior
        print("prioritized behavior is " + str(prioritized_behavior))
        if prioritized_behavior is not None:
            self.bbcon.run_behavior = (prioritized_behavior.motor_recommendations, prioritized_behavior.halt_request)