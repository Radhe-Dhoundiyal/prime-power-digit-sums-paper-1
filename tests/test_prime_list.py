from src.compute_statistics import PRIMES


def test_authoritative_prime_list() -> None:
    assert len(PRIMES) == 50
    assert PRIMES[0] == 2
    assert PRIMES[-1] == 229
    assert len(set(PRIMES)) == 50
