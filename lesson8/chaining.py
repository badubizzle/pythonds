class MyHashTable(object):

    def __init__(self):

        self._data = []
        for i in range(10):
            self._data.append([])

    def _key_hash(self, key):
        """
        Returns integer given a key
        """
        return int(key) % 10

    def insert(self, key, value):
        index = self._key_hash(key)
        bucket = self._data[index]

        for array_tuple in bucket:
            if array_tuple[0] == key:
                raise 'Key exists'

        data = (key, value)
        bucket.append(data)
        self._data[index] = bucket

        # insert("2", 23)
        # insert("12", 3)
        # insert("22", 30)
        # [
        # [("2", 23),("12", 3),("22", 30)]
        # ]
        # get("2") -> [bucket] -> ("2", 23) -> 23
        # get("12")

    def get(self, key):
        index = self._key_hash(key)

        if index < len(self._data):
            if self._data[index] is None:
                raise KeyError

            bucket = self._data[index]
            for array_tuple in bucket:
                if array_tuple[0] == key:
                    return array_tuple[1]

            raise KeyError

            # return self._data[index]
        else:
            raise KeyError

    def update_hash(self, key, value):
        index = self._key_hash(key)
        bucket = self._data[index]

        for array_tuple in bucket:
            if array_tuple[0] == key:
                # import pdb
                # pdb.set_trace()
                array_index = bucket.index(array_tuple)
                bucket[array_index] = (array_tuple[0], value)


h = MyHashTable()

h.insert("2", 50)
h.insert("5", 25)
h.update_hash("2", 45)
h.insert("12", 30)
h.insert("14", 35)

print(h.get("2"))
print(h.get("5"))
print(h.get("12"))
# print(h.get("3"))
