class HotDeskDeepFilter(object):
    def __init__(self):
        self.hotdesk_sandboxes = []
        self.invalid_hotdesks = []
        for i in range(200):
            self.hotdesk_sandboxes.append([])

    def _key_hash(self, key):
        """
        Returns integer given a key
        """

        split_key = key.strip(' ').split(' ')[1]
        return int(split_key)

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

    def insert(self, hotdesk_data):
        key = hotdesk_data['hotdesk']
        index = self._key_hash(key)
        hotdesk_sandbox = self.hotdesk_sandboxes[index]

        parsed_hotdesk_data = {
            'hotdesk': hotdesk_data['hotdesk'].strip(' '),
            'arrival_time': self.get_today_date_time(hotdesk_data['arrival_time']),
            'departure_time': self.get_today_date_time(
                hotdesk_data['departure_time'])
        }

        if self.is_valid_time(hotdesk_data['arrival_time'], hotdesk_data['departure_time']):
            pass
        else:
            self.parse_hotdesk_instance(parsed_hotdesk_data)
            return self.get_invalid_hotdesk_list()

        if len(hotdesk_sandbox) == 0:
            hotdesk_sandbox.append(parsed_hotdesk_data)
            self.hotdesk_sandboxes[index] = hotdesk_sandbox
            return self.get_invalid_hotdesk_list()

        for hotdesk_instance in hotdesk_sandbox:
            # import pdb
            # pdb.set_trace()

            hotdesk_instance_index = hotdesk_sandbox.index(
                hotdesk_instance)

            next_index = hotdesk_instance_index + 1

            sandbox_length = len(hotdesk_sandbox)

            if next_index in range(sandbox_length):
                next_hotdesk = hotdesk_sandbox[next_index]

            if parsed_hotdesk_data['arrival_time'] > hotdesk_instance['departure_time'] and parsed_hotdesk_data['departure_time'] > hotdesk_instance['departure_time'] and next_index not in range(sandbox_length):
                hotdesk_sandbox.append(parsed_hotdesk_data)
                self.hotdesk_sandboxes[index] = hotdesk_sandbox
                return self.get_invalid_hotdesk_list()

            if parsed_hotdesk_data['arrival_time'] < hotdesk_instance['arrival_time'] and parsed_hotdesk_data['departure_time'] < hotdesk_instance['arrival_time']:
                hotdesk_sandbox.insert(0, parsed_hotdesk_data)
                self.hotdesk_sandboxes[index] = hotdesk_sandbox
                return self.get_invalid_hotdesk_list()

            if parsed_hotdesk_data['arrival_time'] > hotdesk_instance['departure_time'] and parsed_hotdesk_data['departure_time'] > hotdesk_instance['departure_time']:

                if next_hotdesk:
                    if parsed_hotdesk_data['arrival_time'] < next_hotdesk['arrival_time'] and parsed_hotdesk_data['departure_time'] < next_hotdesk['arrival_time'] and next_index in range(sandbox_length):
                        hotdesk_sandbox.insert(
                            next_hotdesk, parsed_hotdesk_data)
                        self.hotdesk_sandboxes[index] = hotdesk_sandbox
                        return self.get_invalid_hotdesk_list()

        self.parse_hotdesk_instance(parsed_hotdesk_data)
        self.hotdesk_sandboxes[index] = hotdesk_sandbox
        return self.get_invalid_hotdesk_list()

    def parse_hotdesk_instance(self, hotdesk_instance):
        hotdesk = hotdesk_instance['hotdesk'].strip(' ')
        if hotdesk not in self.invalid_hotdesks:
            self.invalid_hotdesks.append(hotdesk)
        return self.invalid_hotdesks

    def get_invalid_hotdesk_list(self):
        return self.invalid_hotdesks


hotdesks = HotDeskDeepFilter()

hotdesk_schedule = [{
    'hotdesk': ' 1L 15',
    'arrival_time': '10:00:00',
    'departure_time': '12:00:00'
},
    {
    'hotdesk': ' 1L 15',
    'arrival_time': '08:10:00',
    'departure_time': '15:00:00'
},
    {
    'hotdesk': ' 1L 15',
    'arrival_time': '13:10:00',
    'departure_time': '14:00:00'
},
    {
    'hotdesk': ' 1L 15',
    'arrival_time': '08:00:00',
    'departure_time': '9:00:00'
},
    {
    'hotdesk': ' 1L 15',
    'arrival_time': '09:00:00',
    'departure_time': '16:00:00'
},
    {
    'hotdesk': ' 1L 17',
    'arrival_time': '09:00:00',
    'departure_time': '10:00:00'
},
    {
    'hotdesk': ' 1L 17',
    'arrival_time': '11:00:00',
    'departure_time': '12:00:00'
},
    {
    'hotdesk': ' 1L 17',
    'arrival_time': '11:00:00',
    'departure_time': '16:00:00'
}
]

for i in hotdesk_schedule:
    print('inserting this hotdesk .....',  hotdesks.insert(i))
