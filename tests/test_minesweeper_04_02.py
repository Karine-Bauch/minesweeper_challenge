# . should return 0
# * should return *
# .. should return 00
# ** should return **
# .* should return 1*
# *. should return *1


def minesweeper(mines_map: str) -> str:
    if mines_map == '.':
        return '0'
    else:
        return '*'

def test_minesweeper_01() -> None:
    assert minesweeper('.') == '0'

def test_minesweeper_02() -> None:
    assert minesweeper('*') == '*'
