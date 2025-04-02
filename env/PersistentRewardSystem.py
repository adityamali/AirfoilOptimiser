class PersistentRewardSystem:
    def __init__(self):
        self.reward = 0.0
        self.previous_reward = 0.0
        self.reward_history = []

    def AeroReward(self, CL, CD):
        """
        Calculate the aerodynamic reward based on lift and drag coefficients.
        :param CL: Lift coefficient.
        :param CD: Drag coefficient.
        :return: Aerodynamic reward.
        """
        if CD == 0:
            return 0.0
        else:
            return CL / CD

    

H