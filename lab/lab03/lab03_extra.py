from lab03 import *

# Q10
def summation(n, term):
    """Return the sum of the first n terms of a sequence.

    >>> summation(5, lambda x: pow(x, 3))
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up to n.
        use a trick: every time change term's position

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def helper(term0, term1, k):
        if n == k:
            return term0(k)
        return term0(k) + helper(term1, term0, k+1)
    return helper(odd_term, even_term, 1)



