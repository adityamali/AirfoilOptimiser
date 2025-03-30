class ParametricAirfoil:
    def __init__(self):
        self.base_points = 20
        self.constraints = {
            'max_thickness': 0.12,
            'max_camber': 0.05,
            'max_chord_length': 1.0,
        }

    def apply_deltas(self, deltas):
        """
        Apply deltas to the base points of the airfoil.
        :param deltas: List of deltas to apply to the base points.
        :return: List of modified airfoil points.
        """
        if len(deltas) != self.base_points:
            raise ValueError("Number of deltas must match number of base points.")

        modified_points = []

        # TODO: Implement the logic to modify the base points based on deltas provided by the model

        return modified_points