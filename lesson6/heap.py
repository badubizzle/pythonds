class MaxHeap():
    def __init__(self):
        self.heap_data = []

    def insert(self, value):
        self.heap_data.append(value)

        input_index = len(self.heap_data) - 1

        while input_index != 0:
            parent_index = (input_index - 1) // 2

            current_value = self.heap_data[input_index]

            parent_value = self.heap_data[parent_index]

            if current_value > parent_value:

                temp_parent = parent_value
                self.heap_data[parent_index] = current_value

                self.heap_data[input_index] = temp_parent

            input_index = parent_index

    def pop_max(self):

        if len(self.heap_data) == 0:
            return 'Empty list'

        if len(self.heap_data) == 1:
            return self.heap_data.pop()

        popped_data = self.heap_data[0]

        last_element = self.heap_data.pop()

        self.heap_data[0] = last_element

        heap_length = len(self.heap_data)

        current_index = 0

        while current_index < heap_length:
            left_index = (current_index * 2) + 1
            right_index = (current_index * 2) + 2

            left_value = None
            right_value = None

            current_value = self.heap_data[current_index]

            if left_index < heap_length:
                left_value = self.heap_data[left_index]

            if right_index < heap_length:
                right_value = self.heap_data[right_index]

            if left_value is None and right_value is None:
                break

            maximum_index = current_index

            if left_value is not None and left_value > current_value:
                maximum_index = left_index

            if right_value is not None and right_value > self.heap_data[maximum_index]:
                maximum_index = right_index

            if maximum_index != current_index:

                temp_value = self.heap_data[current_index]

                self.heap_data[current_index] = self.heap_data[maximum_index]

                self.heap_data[maximum_index] = temp_value
            elif maximum_index == current_index:
                break

            current_index = maximum_index

        return popped_data

    def sorted_list(self):
        sorted_array = []

        while len(self.heap_data) > 0:
            sorted_array.append(self.pop_max())
        return sorted_array


class MinHeap():
    def __init__(self):
        self.heap_data = []

    def insert(self, value):
        self.heap_data.append(value)

        input_index = len(self.heap_data) - 1

        while input_index != 0:
            parent_index = (input_index - 1) // 2

            current_value = self.heap_data[input_index]

            parent_value = self.heap_data[parent_index]

            if current_value < parent_value:

                temp_parent = parent_value
                self.heap_data[parent_index] = current_value
                # import pdb
                # pdb.set_trace()
                self.heap_data[input_index] = temp_parent

            input_index = parent_index

    def pop_min(self):

        if len(self.heap_data) == 0:
            return 'Empty list'

        if len(self.heap_data) == 1:
            return self.heap_data.pop()

        popped_data = self.heap_data[0]

        last_element = self.heap_data.pop()

        self.heap_data[0] = last_element

        heap_length = len(self.heap_data)

        current_index = 0

        while current_index < heap_length:
            left_index = (current_index * 2) + 1
            right_index = (current_index * 2) + 2

            left_value = None
            right_value = None

            current_value = self.heap_data[current_index]

            if left_index < heap_length:
                left_value = self.heap_data[left_index]

            if right_index < heap_length:
                right_value = self.heap_data[right_index]

            if left_value is None and right_value is None:
                break

            minimum_index = current_index

            if left_value is not None and left_value < current_value:
                minimum_index = left_index

            if right_value is not None and right_value < self.heap_data[minimum_index]:
                minimum_index = right_index

            if minimum_index != current_index:

                temp_value = self.heap_data[current_index]

                self.heap_data[current_index] = self.heap_data[minimum_index]

                self.heap_data[minimum_index] = temp_value
            elif minimum_index == current_index:
                break

            current_index = minimum_index

        return popped_data

    def sorted_list(self):
        sorted_array = []

        while len(self.heap_data) > 0:
            sorted_array.append(self.pop_min())
        return sorted_array


values = [15, 2, 3, 4, 12, 7, 9, 10, 1]

heap = MaxHeap()

for i in values:
    heap.insert(i)
    # print(heap.heap_data)

print(heap.sorted_list())
