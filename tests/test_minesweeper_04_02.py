# . should return 0

def minesweeper(mines_map) -> str:
    pass

def test_minesweeper() -> None:
    data = '.'
    expected = '*'

    assert minesweeper(data) == expected
