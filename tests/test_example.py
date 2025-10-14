import example


def test_square_with_valid_int_returns_square():
    result = example.square(2)
    assert result == 4.0


def test_square_with_valid_float_returns_square():
    result = example.square(2.0)
    assert result == 4.0
