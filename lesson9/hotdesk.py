class HotDeskNode(object):
    def __init__(self, key, hotdesk, arrival_time, departure_time,  next=None, prev=None):
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.hotdesk = hotdesk
        self.key = key
        self.prev = prev
        if isinstance(next, HotDeskNode):
            self.next = next
        else:
            self.next = None


class HotDeskList(object):
    def __init__(self, head=None):
        self.eligible_hot_desks = []
        self.ineligible_hot_desks = []
        if isinstance(head, HotDeskNode):
            self.head = head
        else:
            self.head = None

    def parse_date_time(self, hour, minutes, seconds):
        import datetime
        today = datetime.date.today()
        current_time = datetime.time(hour=hour, minute=minutes)
        return datetime.datetime.combine(today, current_time).strftime('%Y:%m:%d %H:%M')

    def time_parser(self, time_input):
        import datetime
        hour, minutes, seconds = time_input.split(':')
        return int(hour), int(minutes), int(seconds)

    def get_today_date_time(self, time_input):
        hour, minute, second = self.time_parser(time_input)
        convert_to_date_time = self.parse_date_time(hour, minute, second)
        get_datetime = self.parse_string_to_datetime(convert_to_date_time)
        return get_datetime

    def parse_string_to_datetime(self, string_time_input):
        from datetime import datetime
        coverted_date_time = datetime.strptime(
            string_time_input, '%Y:%m:%d %H:%M')
        return coverted_date_time

    def is_valid_time(self, arrival_time, departure_time):
        default_start_time = self.get_today_date_time('07:59:00')
        default_departure_time = self.get_today_date_time('18:00:00')
        input_arrival_time = self.get_today_date_time(arrival_time)
        input_departure_time = self.get_today_date_time(departure_time)
        if input_arrival_time < default_start_time:
            return False
        elif input_arrival_time > default_departure_time:
            return False
        elif input_departure_time > default_departure_time:
            return False
        elif input_departure_time < default_start_time:
            return False
        else:
            return True

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.hotdesk)
            current = current.next

    def get_next(self):
        return self.head.next

    def get_previous(self):
        return self.head.prev

    # def add_hotdesk(self, hotdesk, arrival_time, departure_time):

    def insert_in_empty_hotdesk(self, hotdesk, arrival_time, departure_time):
        if self.head is None:
            new_hotdesk_node = HotDeskNode(
                key, hotdesk, arrival_time, departure_time)
            self.head = new_hotdesk_node
        else:
            print("list is not empty")

    def insert_at_start(self, hotdesk, arrival_time, departure_time):
        if self.head is None:
            new_hotdesk_node = HotDeskNode(
                key, hotdesk, arrival_time, departure_time)
            self.head = new_hotdesk_node
            print("hotdesk inserted")
            return
        new_hotdesk_node = HotDeskNode(
            key, hotdesk, arrival_time, departure_time)
        new_hotdesk_node.next = self.head
        self.head.prev = new_hotdesk_node
        self.head = new_hotdesk_node
        new_hotdesk_node.prev = None

    def insert_at_end(self, hotdesk, arrival_time, departure_time):
        if self.head is None:

            new_hotdesk_node = HotDeskNode(
                hotdesk, arrival_time, departure_time)
            self.head = new_hotdesk_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        new_hotdesk_node = HotDeskNode(
            key, hotdesk, arrival_time, departure_time)
        current_node.next = new_hotdesk_node
        new_hotdesk_node.prev = current_node
        new_hotdesk_node.next = None

    def print_all(self):

        pointer = self.head

        while pointer is not None:
            print(pointer.hotdesk)
            pointer = pointer.next

    def insert_before(self, key, hotdesk, arrival_time, departure_time):
        current_node = self.head
        while current_node is not None:
            if current_node.next is None and current_node.hotdesk


hotdesk = HotDeskList()
# print(hotdesk.is_valid_time('08:00:00', '17:59:00'))


hotdesk.insert_at_end('1L', '11:00:00', '11:59:00')
hotdesk.insert_at_end('1P', '02:00:00', '03:59:00')
hotdesk.insert_at_end('1D', '12:00:00', '15:00:00')
hotdesk.insert_at_start('1U', '13:00:00', '15:00:00')
# hotdesk.insert_before_hotdesk(
#     '1D', '1F', '10:00:00', '15:00:00')
hotdesk.print_all()

# def insert_before_hotdesk(self, previous_hotdesk, hotdesk, arrival_time, departure_time):
#     if self.head is None:
#         print("List is empty")
#         return
#     else:
#         current_node = self.head
#         while current_node is not None:
#             # import pdb
#             # pdb.set_trace()
#             if current_node.hotdesk == previous_hotdesk:
#                 break
#             current_node = current_node.next
#         if current_node is None:
#             print("item not in the list")
#         else:
#             new_hotdesk_node = HotDeskNode(
#                 hotdesk, arrival_time, departure_time)
#             new_hotdesk_node.next = current_node
#             new_hotdesk_node.prev = current_node.prev
#             if current_node.prev is not None:
#                 current_node.prev.next = new_hotdesk_node
#             current_node.next = current_node

# def get_eligible_hotdesks(self):

# def insert_before_item(self, x, data):
#     if self.start_node is None:
#         print("List is empty")
#         return
#     else:
#         n = self.start_node
#         while n is not None:
#             if n.item == x:
#                 break
#             n = n.nref
#         if n is None:
#             print("item not in the list")
#         else:
#             new_node = Node(data)
#             new_node.nref = n
#             new_node.pref = n.pref
#             if n.pref is not None:
#                 n.pref.nref = new_node
#             n.pref = new_node

#     def add_hotdesk(self, hotdesk, arrival_time, departure_time):
#         # import pdb
#         # pdb.set_trace()
#        # if linked list is empty then
#         # make this the head
#         if self.head is None:
#             # create a new node with value
#             # set head to new node
#             new_hotdesk_node = HotDeskNode(
#                 hotdesk, arrival_time, departure_time)
#             self.head = new_hotdesk_node
#             return True
#         if self.is_valid_time(arrival_time, departure_time):
#             pass

#         # if list is not empty
#         # check next node till next node is None
#         # attach new node as next

#         # head = 1
#         current_hot_desk = self.head
#         # import pdb
#         # pdb.set_trace()
#         current_arrival_time = self.get_today_date_time(
#             current_hot_desk.arrival_time)
#         current_departure_time = self.get_today_date_time(
#             current_hot_desk.departure_time)
#         input_arrival_time = self.get_today_date_time(arrival_time)
#         input_departure_time = self.get_today_date_time(departure_time)
#         # import pdb
#         # pdb.set_trace()

#         while current_hot_desk.next is not None:
#             if input_arrival_time < current_arrival_time and input_departure_time < current_arrival_time and current_hot_desk.prev is None:
#                 new_hotdesk_node = HotDeskNode(
#                     hotdesk, arrival_time, departure_time)
#                 current_hot_desk.prev = new_hotdesk_node
#                 # return True
#             elif input_arrival_time < current_arrival_time and input_departure_time < current_arrival_time and current_hot_desk.prev is not None:
#                 temporary_next_node = current_hot_desk
#                 temporary_previous_node = current_hot_desk.prev
#                 new_hotdesk_node = HotDeskNode(
#                     hotdesk, arrival_time, departure_time)
#                 new_hotdesk_node.prev = temporary_previous_node
#                 new_hotdesk_node.next = temporary_next_node
#                 # return True

#         # if current_hot_desk.next is None:
#         #     return True

#         new_hotdesk_node = HotDeskNode(
#             hotdesk, arrival_time, departure_time)
#         temporary_node = current_hot_desk
#         current_hot_desk.next = new_hotdesk_node
#         new_hotdesk_node.prev = temporary_node

#         return False


# def hotdesk_is_first_position(self, arrival_time, departure_time):
#     current_hot_desk = self.head
#     current_arrival_time = self.parse_string_to_datetime(
#         current_hot_desk.arrival_time)
#     current_departure_time = self.parse_string_to_datetime(
#         current_hot_desk.departure_time)
#     input_arrival_time = self.parse_string_to_datetime(arrival_time)
#     input_departure_time = self.parse_string_to_datetime(departure_time)
#     if input_arrival_time < current_arrival_time and input_departure_time < current_arrival_time and current_hot_desk.prev is None:
#         return True
#     return False

# def hotdesk_is_encapsulated(self, arrival_time, departure_time):
#     current_hot_desk = self.head
#     current_arrival_time = self.parse_string_to_datetime(
#         current_hot_desk.arrival_time)
#     current_departure_time = self.parse_string_to_datetime(
#         current_hot_desk.departure_time)
#     input_arrival_time = self.parse_string_to_datetime(arrival_time)
#     input_departure_time = self.parse_string_to_datetime(departure_time)
#     if input_arrival_time < current_arrival_time and input_departure_time < current_arrival_time and current_hot_desk.prev is not None:
#         return True
#     return False

# def at_end_of_list(self, arrival_time, departure_time):
#     current_hot_desk = self.head

# def is_valid_time(self, arrival_time, departure_time):
#     default_start_time = get_today_date_time('08:00:00')
#     default_departure_time = get_today_date_time('18:00:00')
#     if arrival_time < default_start_time and arrival_time > default_departure_time and departure_time > default_departure_time and departure_time < default_start_time:
#         return False
#     return True

# def time_parser(time_input):
#     import datetime
#     hour, minutes, seconds = time_input.split(':')
#     return int(hour), int(minutes), int(seconds)

# def parse_date_time(hour, minutes, seconds):
#     import datetime
#     today = datetime.date.today()
#     current_time = datetime.time(hour=hour, minute=minutes)
#     return datetime.datetime.combine(today, current_time).strftime('%Y:%m:%d %H:%M')

# def set_time(arrival_time, departure_time):
#     arrival_hour, arrival_minute, arrival_second = time_parser(
#         arrival_time)
#     departure_hour, departure_minute, departure_second = time_parser(
#         departure_time)
#     arrival_time = parse_date_time(
#         arrival_hour, arrival_minute, arrival_second)
#     departure_time = parse_date_time(
#         departure_hour, departure_minute, departure_second)

#     return arrival_time, departure_time

# def get_today_date_time(time_input):
#     hour, minute, second = time_parser(time_input)
#     convert_to_date_time = parse_date_time(hour, minute, second)
#     # import pdb
#     # pdb.set_trace()
#     get_datetime = parse_string_to_datetime(convert_to_date_time)
#     return get_datetime

# def is_valid_time(arrival_time, departure_time):
#     default_start_time = get_today_date_time('07:59:00')
#     default_departure_time = get_today_date_time('18:00:00')
#     input_arrival_time = get_today_date_time(arrival_time)
#     input_departure_time = get_today_date_time(departure_time)
#     if input_arrival_time < default_start_time:
#         return False
#     elif input_arrival_time > default_departure_time:
#         return False
#     elif input_departure_time > default_departure_time:
#         return False
#     elif input_departure_time < default_start_time:
#         return False
#     else:
#         return True

# print(is_valid_time('08:00:00', '17:59:00'))

# pras = time_parser('9:59:00')

# print(set_time('08:00:00', '9:59:00'))

# print('adding hotdesk', hotdesk.add_hotdesk())
