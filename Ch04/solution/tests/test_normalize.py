import numpy as np

import normalize

def test_by_zscore():
    data = np.random.normal(0, 10, 1000)
    i, j = 93, 576
    data[i], data[j] = 1076, -5327
    mean = data.mean()

    out = normalize.by_zscore(data)
    assert out[i] == out[j] == mean
