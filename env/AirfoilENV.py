import gymnasium
import numpy as np
from gymnasium import spaces

from HybridCFDProxy import HybridCFDProxy
from CoordinateAirfoil import CoordinateAirfoil
from PersistentRewardSystem import PersistentRewardSystem

class AirfoilENV(gymnasium.Env):
    """
    Custom Environment for RL agent to modify airfoil shape and recieve rewards based on aerodynamic performance.
    """

    def __init__(self, config=None):
        super(AirfoilENV, self).__init__()

        self.config = {
            # TODO: Define the standard configuration for the airfoil
        }

        self.airfoil = CoordinateAirfoil()
        self.simulator = HybridCFDProxy()
        self.reward_system = PersistentRewardSystem()

        if config:
            self.config.update(config)

    def reset(self):
        # TODO: Reset the environment to its initial state
        pass

    def step(self, action):
        # TODO: Implement the logic for taking a step in the environment
        pass

    def _get_observation(self):
       # TODO: Implement method to construct the observation from the current state
        pass

    def _evaluate_airfoil(self):
        # TODO: Implement method to work with the @HybridCFDProxy to evaluate the airfoil
        pass

    def _calculate_reward(self):
        # TODO: Implement method to calculate the reward using @PersistentRewardSystem
        pass

    def render(self):
        # TODO:  Implement rendering logic for visualisation using @Visualiser and @CoordinateAirfoil
        pass

    def close(self):
        """Close the environment."""
        pass


        
    
