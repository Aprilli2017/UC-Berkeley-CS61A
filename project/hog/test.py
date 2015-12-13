def free_bacon(opponent_score):
    """ Get one more than the largest digit in the opponent's total score

        >>> free_bacon(42)
        5
        >>> free_bacon(48)
        9
        >>> free_bacon(7)
        8
    """
    assert 0 <= opponent_score <= 99
    return 1 + max(opponent_score // 10, opponent_score % 10)

def is_prime(score):
    """ 
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    >>> is_prime(100)
    False
    >>> is_prime(13)
    True
    """
    assert score >= 0
    if score <= 1:
        return False
    i = 2
    while i < score:
        if score % i == 0:
            return False
        i += 1
    return True

def next_prime(score):
    """ 
    score must a prime
    >>> next_prime(13)
    17
    >>> next_prime(11)
    13
    """
    while True:
        score += 1
        if is_prime(score):
            return score



