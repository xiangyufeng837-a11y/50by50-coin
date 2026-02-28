import secrets


def flip_coin() -> str:
    """Flip a fair coin using a cryptographically secure RNG.

    Returns:
        "Heads" or "Tails" with equal probability.
    """
    # secrets.choice gives unbiased selection from sequence
    return secrets.choice(["Heads", "Tails"])


if __name__ == "__main__":
    # simple command-line invocation
    result = flip_coin()
    print(f"Coin toss result: {result}")
