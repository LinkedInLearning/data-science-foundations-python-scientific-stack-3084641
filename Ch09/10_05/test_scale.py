import numpy as np

from scale import scale


def test_simple():
    v = np.array([0.1, np.nan, 1.1])
    n = 1.1
    expected = np.array([0.11, np.nan, 1.21])
    out = scale(v, n)
    assert np.allclose(expected, out, equal_nan=True)