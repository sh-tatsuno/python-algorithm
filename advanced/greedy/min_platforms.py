def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    so that no train has to wait for other(s) to leave
    """
    arrival = sorted(arrival)
    departure = sorted(departure)
    
    platforms = 0
    waits = 0
    aind = 0
    dind = 0
    while(dind < len(departure) and aind < len(arrival)):
        if arrival[aind] < departure[dind]:
            waits += 1
            aind += 1
            if waits > platforms:
                platforms = waits
        else:
            dind += 1
            waits -=1
    
    return platforms

def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]
    
    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)