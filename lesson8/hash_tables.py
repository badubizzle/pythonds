class MyHashTable(object):

    def __init__(self):

        self._data = [None] * 10
    
    def _key_hash(self, key):
        """
        Returns integer given a key
        """        
        return int(key) % 10


    def insert(self, key, value):        
        index = self._key_hash(key)
        if index < len(self._data):
            self._data[index] = value
        else:
            raise KeyError

        # if index < len(self._data):
        #     self._data[index] = value
        # else:
        #     self._data = self._expand_data(index)
        #     self._data[index] = value

        
    # def _expand_data(self, index):

    #     temp = self._data.copy()

    #     while len(temp) < index:
    #         temp.append(None)
        
        
    #     return temp


    def get(self, key):
        index = self._key_hash(key)
        
        if index < len(self._data):
            if self._data[index] is None:
                raise KeyError
                
            return self._data[index]
        else:
            raise KeyError


h = MyHashTable()

h.insert("2", 50)
h.insert("5", 25)

print(h.get("2"))
print(h.get("5"))
print(h.get("3"))



