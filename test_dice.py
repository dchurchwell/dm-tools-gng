from dice import *

for i in range (50):
    assert d(20) > 0
    assert d(20) < 21
    result = roll("8d6+20 + 2d8 - 10 +   1d20+5")
    assert result > 25
    assert result < 100

    result = roll("8d6 fire + 2d6 BLudgeoning + 10 lightning")
    assert result['fire'] >= 8
    assert result['fire'] <= 48
    assert result['bludgeoning'] >= 2
    assert result['bludgeoning'] <= 12
    assert result['lightning'] == 10