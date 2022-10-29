def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    s = range(A, B + 1)
    z = list(s)
    return list(z)[::-1]

print(main(3, 7))