def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    s = 0

    for s in range(A, B):
        s += range(A, B)
    return s