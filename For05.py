def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    s = range(B + 1, A)
    return list(s)

print(main(3, 1))