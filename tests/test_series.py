from math_series.series import fibonacci,lucas,sum_series

def test_fibonacci():
    excepted=1
    acctualy=fibonacci(1)
    assert acctualy==excepted

def test_fibonacci_sixith():
    excepted=8
    acctualy=fibonacci(6)
    assert acctualy==excepted


def test_lucas_zero():
    excepted=2
    acctualy=lucas(0)
    assert acctualy==excepted

def test_lucas_third():
    excepted=4
    acctualy=lucas(3)
    assert acctualy==excepted


def test_sum_series_sixth():
    excepted=8
    acctualy=sum_series(6)
    assert acctualy==excepted

def test_sum_series_first():
    excepted=1
    acctualy=sum_series(1)
    assert acctualy==excepted


