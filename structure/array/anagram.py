def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    word_dict = {}
    for s in str1.lower():
        if s != ' ':
            word_dict[s] = word_dict.get(s,0)
            word_dict[s] +=1
    
    for s in str2.lower():
        if s != ' ':
            if s in word_dict:
                word_dict[s] -=1
                if word_dict[s] < 0 :
                    return False
            else:
                return False
    
    return True