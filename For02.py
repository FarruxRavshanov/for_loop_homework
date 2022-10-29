def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    z = ""
    a = range(0, n)
    for i in range(a):
        z += str(i) + ','
    
    return z[:-1]