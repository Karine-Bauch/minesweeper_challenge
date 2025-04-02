# . should return 0
# * should return *
# .. should return 00
# ** should return **
# .* should return 1*
# *. should return *1


def minesweeper(mines_map: str) -> str:
    result = ''
    for i in mines_map:
        if i == '.':
            result += '0'
        if i == '*':
            result += '*'
    return result

def test_minesweeper_01() -> None:
    assert minesweeper('.') == '0'

def test_minesweeper_02() -> None:
    assert minesweeper('*') == '*'

def test_minesweeper_03() -> None:
    assert minesweeper('..') == '00'