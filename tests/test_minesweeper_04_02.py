# . should return 0


def minesweeper(mines_map) -> str:
    return '0'

def test_minesweeper() -> None:
    data = '.'
    expected = '0'

    assert minesweeper(data) == expected
