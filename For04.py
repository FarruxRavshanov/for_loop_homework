def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    c = range(A, B + 1)
    return list(c)

print(main(2, 7))