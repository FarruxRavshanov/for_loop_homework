def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    s = range(B, A + 1)
    return list(s)[::-1]

print(main(3, 7))