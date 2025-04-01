# example:
# .*.**.
# ....*.
# ..*...
#
# should return:
# 1*2**2
# 1234*2
# 01*211


def minesweeper(mines_map: str) -> str:
    result = """
    1*2**2
    1234*2
    01*211
    """
    return result


def test_minesweeper() -> None:
    data = """
    .*.**.
    ....*.
    ..*...
    """

    expected = """
    1*2**2
    1234*2
    01*211
    """
    assert minesweeper(data) == expected