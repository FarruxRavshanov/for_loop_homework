def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    z = ""
    for i in range(0,n):
        z += str(i) + ','
    
    return z[:-1]