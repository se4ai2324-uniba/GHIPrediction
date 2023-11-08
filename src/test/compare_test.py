"""module containing testing functions for compare module"""
import sys
sys.path.insert(0, "src/models/")
from compare import compare_r2, compare

def test_compare_r2():
    """testing function for compare_r2"""
    array1 = [0.82, 110.0]
    array2 = [0.82, 110.0]
    array3 = [0.82, 110.0]
    array4 = [0.82, 110.0]
    best = compare_r2(array1, array2, array3, array4)

    assert best is not None
    assert isinstance(best, list)

def test_compare():
    """testing function for comparison"""
    best = [0.86, 113.0]
    rf = ["rf", 0.82, 110.0]
    xgb = ["xgb", 0.82, 110.0]
    lr = ["lr", 0.82, 110.0]
    knr = ["knr", 0.82, 110.0]
    model_best = compare(best, rf,xgb,lr,knr)

    assert isinstance(model_best, str)
    assert model_best is not None
