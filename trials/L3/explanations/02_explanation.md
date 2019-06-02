This solution is simlar to problem_01, using binary search and narrowing the range.  
Specifically, this input array is not sorted, so I spilit the program in some cases.  
I consider in the cases of the center value.   
1. lower value < (center value, number) < upper value: normal order
2. lower value > upper value
   1. lower value < center value & upper value < center value
   2. center value < lower value & center value < upper value

The order is O(logN), because it is like binary search.  
test is covered 5 cases.