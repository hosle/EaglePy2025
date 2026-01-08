from design_hit_counter import HitCounter
import pytest


def test_case():
    obj = HitCounter()
    obj.hit(1)
    obj.hit(2)
    obj.hit(3)

    assert obj.getHits(4) == 3

    obj.hit(300)

    assert obj.getHits(300) == 4
    assert obj.getHits(301) == 3


# def test_case():
#     obj = HitCounter()
#     obj.hit(1)
#     obj.hit(2)
#     obj.hit(3)
#
#     assert obj.getHits(4) == 3
#
#     obj.hit(300)
#
#     assert obj.getHits(300) == 4
#     assert obj.getHits(301) == 3
