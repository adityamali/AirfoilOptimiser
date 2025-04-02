import gym
import numpy as np
from gymnasium import spaces

from HybridCFDProxy import HybridCFDProxy
from CSTAirfoil import CSTAirfoil
from PersistentRewardSystem import PersistentRewardSystem

class AirfoilENV(gym.Env):
    """
    Custom Environment for RL agent to modify airfoil shape and recieve rewards based on aerodynamic performance.
    """

    def __init__(self, config=None):
        super(AirfoilENV, self).__init__()

        self.config = {
            # TODO: Define the standard configuration for the airfoil
        }

        self.airfoil = CSTAirfoil()
        self.simulator = HybridCFDProxy()
        self.reward_system = PersistentRewardSystem()

        if config:
            self.config.update(config)

        
    
