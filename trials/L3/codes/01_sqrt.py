def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    def search_sqrt(number, upper, lower):
        current = (upper + lower) // 2
        if current ** 2 > number:
            upper = current
        elif current ** 2 == number:
            return current
        else:  # current ** 2 < number
            lower = current

        if upper - lower <= 1:
            return lower

        return search_sqrt(number, upper, lower)

    if number ** 2 == number:
        return number

    return search_sqrt(number, number, 0)


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
