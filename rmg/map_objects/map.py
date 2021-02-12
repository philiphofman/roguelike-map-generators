from rmg.map_objects.tile import Tile


class Map:
    """Map stores Tiles in a 2D array."""

    def __init__(self, width, height):
        """Inits values for the map.

        Args:
            width(int): An integer defining the width of the map.
            height(int): An integer defining the height of the map.
        """

        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        """Creates a 2D array of tiles with own width and height.

        By default every tile blocks movement.

        Returns:
            tiles(list): A 2D array of tiles with the dimensions of the GameMap
                object.
        """

        tiles = [[Tile(True) for y in range(self.height)] for x in
                 range(self.width)]

        return tiles
