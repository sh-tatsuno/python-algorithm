class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        ind = self.calculate_hash_value(string)
        if (ind < 0) or (ind > len(self.table)):
            return -1
        if self.table[ind] == None:
            self.table[ind] = [string]
        else:
            st = set(self.table[ind])
            st.add(string)
            self.table[ind] = list(st)
                

    def lookup(self, string):
        ind = self.calculate_hash_value(string)
        if (ind < 0) or (ind > len(self.table)):
            return -1
        if self.table[ind] == None:
            return -1
        else:
            return self.calculate_hash_value(string) if string in self.table[ind] else -1

    def calculate_hash_value(self, string):
        if len(string) < 1:
            return -1
        if len(string) ==1:
            return ord(string)
        
        return ord(string[0]) * 100 + ord(string[1])

# test case
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))
