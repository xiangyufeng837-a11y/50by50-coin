import pytest
from coin_flip import flip_coin


def test_flip_distribution():
    # Run a large number of flips to check approximate distribution
    counts = {"Heads": 0, "Tails": 0}
    trials = 100000
    for _ in range(trials):
        counts[flip_coin()] += 1
    # proportion should be close to 0.5
    heads_ratio = counts["Heads"] / trials
    tails_ratio = counts["Tails"] / trials
    assert 0.49 < heads_ratio < 0.51
    assert 0.49 < tails_ratio < 0.51
