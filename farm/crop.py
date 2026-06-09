# pylint: disable=too-few-public-methods
"""Module defining the base Crop class shared by all crop types."""


class Crop:
    """A generic crop with grain count and ripeness logic."""

    def __init__(self):
        self.grains = 0

    def ripe(self):
        """Return True when the crop has at least 15 grains."""
        return self.grains >= 15
