def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    list1 = list(range(A, B))
    i = 0
    s = 0

    while i < len(list1):
        s += list1[i]
        i += 1
    return s

print(main(3, 6))