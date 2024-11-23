class HashTable:
    def __init__(self, size):
        
        self.size = size
        self.table = [[] for _ in range(size)]  # create a list of empty lists for buckets.


    def get(self, key):
        
        index = key % self.size
        indexValue = self.table[index]
        
        for k, v in indexValue: # check if the key exist in the hashtable
            if k == key:
                return v
        
        return None  # return none if the key not ffound
    
    def set(self, key, value):
        
        index = self._hash(key)
        indexValue = self.table[index]
        
        
        for i, (k, v) in enumerate(indexValue): # check if the key exist in the hashtable
            if k == key:
                indexValue[i] = (key, value)  # if the key exist in the hashtable, update it.
                return
        
        
        indexValue.append((key, value)) # if the key does not exist, add new one.

    

# Example usage
table = HashTable(5)
table.set(238, "hello") # 238 % 5 = 3 
table.set(5251, "world")  # 5251 % 5 = 1
table.set(123, "good")  # 123 % 5 = 3 (collision with 238)

# Retrieving values
print(table.get(238))   # Output: hello
print(table.get(5251))  # Output: world
print(table.get(123))   # Output: good
print(table.get(22))    # Output: None
