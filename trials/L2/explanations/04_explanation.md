I have implemented active directory by very similar method of file recursion.  

I search each depth of the tree of parent directory, so I look up user name by dfs.  
The order should be O(NlogN) and the number of cases is 3.