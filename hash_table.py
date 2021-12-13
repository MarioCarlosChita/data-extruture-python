class HashTable:

    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(1, self.Max)]

    def get_hash(self, key):
        sum = 0
        for v in key:
            sum += ord(v)
        return sum % self.Max

    def Add (self , key  , val): 
        self.arr[self.get_hash(key)] =val;

    def getElement(self, key):
        return self.arr[self.get_hash(key)];

