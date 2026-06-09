"""Module defining the Corn crop."""

from farm.crop import Crop


class Corn(Crop):
    """A corn crop that gains 10 grains per watering."""

    def water(self):
        """Add 10 grains to the corn crop."""
        self.grains += 10
