"""module containing testing functions for compare module"""
import sys
import pytest
sys.path.insert(0, "src/models/")
from compare import compare_r2, compare, linear, random_forest, xgb_metrics, knr

@pytest.fixture
def testing_compare_r2():
    """needed to import models results as fixtures"""
    return compare_r2

@pytest.fixture
def testing_compare():
    """needed to import models results as fixtures"""
    return compare

@pytest.fixture
def testing_linear():
    """needed to import models results as fixtures"""
    return linear

@pytest.fixture
def testing_rf():
    """needed to import models results as fixtures"""
    return random_forest

@pytest.fixture
def testing_xgb():
    """needed to import models results as fixtures"""
    return xgb_metrics

@pytest.fixture
def testing_knr():
    """needed to import models results as fixtures"""
    return knr

def test_compare_r2(testing_linear, testing_rf, testing_xgb, testing_knr):
    """testing function for compare_r2"""
    best = compare_r2(testing_linear, testing_rf, testing_xgb, testing_knr)
    assert best is not None
    assert isinstance(best, list)

def test_compare(testing_compare_r2, testing_linear, testing_rf, testing_xgb, testing_knr):
    """testing function for comparison"""
    best = testing_compare_r2(testing_linear, testing_rf, testing_xgb, testing_knr)
    model_best = compare(best, testing_linear, testing_rf, testing_xgb, testing_knr)

    assert isinstance(model_best, str)
    assert model_best is not None
