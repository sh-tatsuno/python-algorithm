wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
def bubble_sort_1(l):
    flag=True
    while(flag):
        flag = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                tmp = l[i]
                l[i] = l[i+1]
                l[i+1] = tmp
                flag = True
    return l

bubble_sort_1(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l):
    flag=True
    while(flag):
        flag = False
        for i in range(len(l)-1):
            if l[i][0] < l[i+1][0]:
                tmp = l[i]
                l[i] = l[i+1]
                l[i+1] = tmp
                flag = True
            elif l[i][0] == l[i+1][0] and l[i][1] < l[i+1][1]:
                tmp = l[i]
                l[i] = l[i+1]
                l[i+1] = tmp
                flag = True
    return l

bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")