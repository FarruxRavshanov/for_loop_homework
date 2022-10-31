def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    list1 = list(range(0, N))
    i = 0
    s = 0

    while i < len(list1):
        if list1[i] % 2 == 1:
            s += list1[i]
        i += 1
    return s