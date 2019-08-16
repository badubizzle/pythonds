class MyHashTable(object):

    def __init__(self):

        self._data = []
        for i in range(10):
            self._data.append([])

    def create_sandboxes(self, list_number):
        self.length = list_number
        for i in range(list_number):
            self._data.append([])
        return

    def _key_hash(self, key):
        """
        Returns integer given a key
        """
        # self.create_sandboxes(20)
        import pdb
        pdb.set_trace()
        return key.split(' ')[1]

    def insert(self, key, value, max_number):
        index = self._key_hash(key)
        bucket = self._data[index]

        for array_tuple in bucket:
            if array_tuple[0] == key:
                raise 'Key exists'

        data = (key, value)
        bucket.append(data)
        self._data[index] = bucket
        import pdb
        pdb.set_trace()

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

    def hotdesk_length(self, hotdesk_array):
        hotdesk_count = 0
        stripped_hotdesks = []
        for hot_desk in hotdesk_array:
            strip_hotdesk = hot_desk.strip(' ')
            stripped_hotdesks.append(strip_hotdesk)
            hotdesk_count += 1
        return hotdesk_count, stripped_hotdesks
