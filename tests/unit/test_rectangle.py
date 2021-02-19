from map_objects.rectangle import Rect


def test_class_initialization():
    expected_x1 = 0
    expected_y1 = 0
    expected_w = 5
    expected_h = 4

    rect1 = Rect(expected_x1, expected_y1, expected_w, expected_h)

    assert rect1.x1 == expected_x1
    assert rect1.y1 == expected_y1
    assert rect1.x2 == expected_x1 + expected_w
    assert rect1.y2 == expected_y1 + expected_h


def test_center():
    expected_x1 = 0
    expected_y1 = 0
    expected_w = 5
    expected_h = 4

    rect1 = Rect(expected_x1, expected_y1, expected_w, expected_h)

    assert rect1.center() == (int((expected_x1 + expected_w) / 2),
                              int((expected_y1 + expected_h) / 2))


def test_intersect():
    expected_a_x1 = 0
    expected_a_y1 = 0
    expected_a_w = 5
    expected_a_h = 4

    expected_b_x1 = 6
    expected_b_y1 = 6
    expected_b_w = 2
    expected_b_h = 2

    expected_c_x1 = 4
    expected_c_y1 = 3
    expected_c_w = 3
    expected_c_h = 4

    rect1 = Rect(expected_a_x1, expected_a_y1, expected_a_w, expected_a_h)
    rect2 = Rect(expected_b_x1, expected_b_y1, expected_b_w, expected_b_h)
    rect3 = Rect(expected_c_x1, expected_c_y1, expected_c_w, expected_c_h)

    assert rect1.intersect(rect2) is False
    assert rect1.intersect(rect3) is True
    assert rect2.intersect(rect3) is True
