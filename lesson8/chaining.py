class MyHashTable(object):

    def __init__(self):

        self._data = [[]] * 10
    
    def _key_hash(self, key):
        """
        Returns integer given a key
        """        
        return int(key) % 10

    def insert(self, key, value):        
        index = self._key_hash(key)
        bucket = self._data[index]

        data = (key, value)
        bucket.append(data)
        self._data[index] = bucket
        


        # insert("2", 23)
        # insert("12", 3)
        # insert("22", 30)
        #[
        # [("2", 23),("12", 3),("22", 30)]
        # ]
        # get("2") -> [bucket] -> ("2", 23) -> 23
        # get("12")

        


    def get(self, key):
        index = self._key_hash(key)
        
        if index < len(self._data):
            if self._data[index] is None:
                raise KeyError
                
            return self._data[index]
        else:
            raise KeyError