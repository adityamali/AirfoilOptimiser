from tkinter import *
from HybridCFDProxy import HybridCFDProxy
from ParametricAirfoil import ParametricAirfoil
from PersistentRewardSystem import PersistentRewardSystem


class EnvMain:
    def __init__(self):
        self.root = Tk()
        self.root.title("AirFoil Learner")
        self.root.geometry("800x600")
        self.root.mainloop()

        self.shape_generator = ParametricAirfoil()
        self.simulator = HybridCFDProxy()
        self.reward_calculator = PersistentRewardSystem()

    

if __name__ == "__main__":
    EnvMain()