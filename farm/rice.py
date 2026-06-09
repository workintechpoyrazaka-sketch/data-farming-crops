"""Module defining the Rice crop."""

from farm.crop import Crop


class Rice(Crop):
    """A rice crop that gains 5 grains per watering and 10 per transplant."""

    def water(self):
        """Add 5 grains to the rice crop."""
        self.grains += 5

    def transplant(self):
        """Add 10 grains to the rice crop."""
        self.grains += 10
