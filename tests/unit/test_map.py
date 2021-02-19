from map_objects.map import Map


def test_class_initialization():
    m1 = Map(5, 5)

    expected_width = 5
    expected_height = 5

    assert m1.width == expected_width
    assert m1.height == expected_height

    assert len(m1.tiles) == expected_height

    for x_row in m1.tiles:
        assert len(x_row) == expected_width

        for tile in x_row:
            expected_blocked = True
            expected_block_sight = True
            expected_explored = False

            assert tile.blocked == expected_blocked
            assert tile.block_sight == expected_block_sight
            assert tile.explored == expected_explored
