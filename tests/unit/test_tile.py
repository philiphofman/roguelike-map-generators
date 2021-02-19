from map_objects.tile import Tile


def test_default_values():
    t1 = Tile(True)
    expected_blocked = True
    expected_block_sight = True
    expected_explored = False

    assert t1.blocked == expected_blocked
    assert t1.block_sight == expected_block_sight
    assert t1.explored == expected_explored


def test_custom_values():
    t1 = Tile(True, False)
    expected_blocked = True
    expected_block_sight = False
    expected_explored = False

    assert t1.blocked == expected_blocked
    assert t1.block_sight == expected_block_sight
    assert t1.explored == expected_explored
