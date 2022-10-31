def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    list1 = list(0, N)
    sum = 0
    i = 0

    while i < len(list1):
        sum += 1 / list1[i]
    return sum