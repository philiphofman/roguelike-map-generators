from map_objects.tile import Tile


class Map:
    """A 2D array of Tile objects.

    The Map class stores Tile objects in a 2D array to create a
    basic top-down map. It also includes some helper functions to
    streamline basic interactions such as creating rooms and corridors.

    Attributes:
        width (int): The int width (x) of the map.
        height (int): The int height (y) of the map.
        tiles (List): The 2D array of Tile objects.
    """

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

        By default every tile blocks movement and sight. The 2D array
        is a nested list, with x being the top level list, and y being
        the nested list, like so:

        x0 -> [[y0, y1, y2],
        x1 ->  [y0, y1, y2],
        x2 ->  [y0, y1, y2]]

        Returns:
            tiles(list): A 2D array of tiles with the dimensions of the Map
                object.
        """

        tiles = [[Tile(True) for y in range(self.height)] for x in
                 range(self.width)]

        return tiles

    def create_room(self, room):
        """Goes through the tiles in a room and unblocks them.

        The function leaves a one-tile-wide wall around the room,
        so if the room is 5x5, the walkable floor space will measure
        4x4.

        Args:
            room(Rect): A Rect object representing the room.
        """

        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        """Creates a horizontal tunnel.

        Args:
            x1(int): The starting point.
            x2(int): The end point.
            y(int): Which row to use.
        """

        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False
