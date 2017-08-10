"""
Implement a hash-map/hash-table (with chaining).
"""

def hash_function(key_string, capacity):
    '''Returns a hash corresponding to the index of a given key and given size of the table'''
    hash_val = 7 # choose a prime number as a seed
    for char in key_string:
        hash_val = 31 * hash_val + ord(char) # pick a hash function that is evenly distributed
    return hash_val % capacity

class HashMapWithChaining(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [[] for i in range(capacity)]

    def put(self, key, value):
        index = hash_function(key, self.capacity)
        hash_cell = self.data[index]
        for i in hash_cell:
            if i[0] == key:
                i[1] = value
                return
        hash_cell.append([key, value])
        self.size += 1
        if self.size >= self.capacity * 0.75: # if size is close to 75% of capacity -> double
            self.double_table_size()

    def get(self, key):
        index = hash_function(key, self.capacity)
        hash_cell = self.data[index]
        for i in hash_cell:
            if i[0] == key:
                return i[1]
        raise KeyError(key)

    def remove(self, key):
        index = hash_function(key, self.capacity)
        hash_cell = self.data[index]
        for i in range(len(hash_cell)):
            if hash_cell[i][0] == key:
                hash_cell.pop(i)
                self.size -= 1
                return
        raise KeyError(key)

    def contains(self, key):
        index = hash_function(key, self.capacity)
        hash_cell = self.data[index]
        for i in hash_cell:
            if i[0] == key:
                return True
        return False

    def keys(self):
        return [j[0] for i in self.data for j in i if j]

    def __repr__(self):
        return str(self.data)

    def double_table_size(self):
        new_capacity = self.get_next_prime(2*self.capacity) # double to the next available prime
        new_data = [[] for i in range(new_capacity)]
        for key in self.keys():
            new_data[hash_function(key, new_capacity)].append([key, self.get(key)])
        self.data = new_data
        self.capacity = new_capacity

    def get_next_prime(self, num):
        if num % 2 == 0:
            num += 1
        while not self.is_prime(num):
            num += 2
        return num

    def is_prime(self, num):
        for i in range(2, num, 2):
            if num % i == 0:
                return False
        return True
