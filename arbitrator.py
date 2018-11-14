class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        #active_behaviors = filter(lambda x: x.active_flag == True, self.bbcon.behaviors)
        prioritized_behavior = None
        #if len(self.bbcon.active_behaviors) == 0:
         #   self.bbcon.run_behavior = (None , True)
          #  return
        for behavior in self.bbcon.active_behaviors:
            if prioritized_behavior is None or prioritized_behavior.weight < behavior.weight:
                prioritized_behavior = behavior
        if prioritized_behavior is not None:
            self.bbcon.run_behavior = (prioritized_behavior.motor_recommendations, prioritized_behavior.halt_request)
            #self.bbcon.run_behavior = prioritized_behavior.motor_recommendations