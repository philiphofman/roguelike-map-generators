"""
A tile on a map. It may or may not be blocked, and may or may not block sight.
"""


class Tile:
    """The Tile class is the basic building block of maps.

    Attributes:
        blocked (bool): Whether the tile blocks movement.
        block_sight (bool): Whether the tile blocks sight.
        explored (bool): Whether the tile has been explored.
    """

    def __init__(self, blocked, block_sight=None):
        """Inits default values for this Tile.

        Sets 'blocked' to its passed value. If 'block_sight' isn't set to a
        value, it's automatically set to the same value as 'blocked'. Explored
        is always set to false.

        Args:
            blocked(bool): Indicates if this tile blocks movement.
            block_sight(bool): Indicates if this tile blocks sight.
        """

        self.blocked = blocked

        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight

        self.explored = False
