""""
Hash Map with Open Addressing (<- a type of collision resolution)
Collision Resolution: Open Addressing w/ Linear Probing
"""

def hash_function(num, capacity):
    return num % capacity

def rehash(idx, capacity):
    return (idx + 1) % capacity

class HashMap(object):
    def __init__(self, capacity=11):
        self.capacity = capacity
        self.slots = [None] * self.capacity # keys
        self.data = [None] * self.capacity # values

    def put(self, key, value):
        index = hash_function(key, self.capacity)
        if self.slots[index] == None:
            self.slots[index] = key
            self.data[index] = value
        else:
            if self.slots[index] == key:
                self.data[index] = value
            else:
                next_slot = rehash(index, self.capacity)
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = rehash(next_slot, self.capacity)
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = value

    def get(self, key):
        index = hash_function(key, self.capacity)
        if self.slots[index] == key:
            return self.data[index]
        else:
            next_slot = rehash(index, self.capacity)
            start = next_slot
            while self.slots[next_slot] != key and start != next_slot:
                next_slot = rehash(next_slot, self.capacity)
            if self.slots[next_slot] == key:
                return self.data[next_slot]
            raise KeyError(key)

    def __repr__(self):
        return str(self.slots) + '\n' + str(self.data)
