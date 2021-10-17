import dice

def test_build_dice_number_of_dice():
    dice_str = "10d1"
    d = dice.utils.build_dice(dice_str)
    assert len(d.dice) == 10

def test_build_dice_number_of_dice_unspecified():
    dice_str = "d1"
    d = dice.utils.build_dice(dice_str)
    assert len(d.dice) == 1
