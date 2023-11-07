import pandas as pd
import sys
sys.path.insert(0, "src/models/")
from compare import compare_r2, compare

def test_compare_r2():
    array1 = [0.82, 110.0]
    array2 = [0.82, 110.0]
    array3 = [0.82, 110.0]
    array4 = [0.82, 110.0]
    best = compare_r2(array1, array2, array3, array4)

    assert best is not None
    assert isinstance(best, list)


def test_compare():
    best = [0.86, 113.0]
    rf = ["rf", 0.82, 110.0]
    xgb = ["xgb", 0.82, 110.0]
    lr = ["lr", 0.82, 110.0]
    knr = ["knr", 0.82, 110.0]

    modelBest = compare(best, rf,xgb,lr,knr)

    assert isinstance(modelBest, str)
    assert modelBest is not None
