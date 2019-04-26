# Code

def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    
    if len(str1)!=len(str2): 
        return None
    
    # TODO: Write your solution here
    dist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]: dist += 1
    
    return dist