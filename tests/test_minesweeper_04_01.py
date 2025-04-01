# example:
# .*.**.
# ....*.
# ..*...
#
# should return:
# 1*2**2
# 1234*2
# 01*211

def test_minesweeper():
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