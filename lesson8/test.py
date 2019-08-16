def time_parser(time_input):
    hour, minutes, seconds = time_input.split(':')
    return int(hour), int(minutes), int(seconds)


def parse_date_time(hour, minutes, seconds):
    import datetime
    today = datetime.date.today()
    current_time = datetime.time(hour=hour, minute=minutes)
    return datetime.datetime.combine(today, current_time).strftime('%Y-%m-%d %H:%M')


# def parse_string_time(string_time_input):
#     from datetime import datetime
#     coverted_date_time = datetime.strptime(
#         string_time_input, '%Y-%m-%d %H:%M')
#     return coverted_date_time

def parse_string_to_datetime(string_time_input):
    from datetime import datetime
    coverted_date_time = datetime.strptime(
        string_time_input, '%Y-%m-%d %H:%M')
    return coverted_date_time


def set_time(arrival_time, departure_time):
    arrival_hour, arrival_minute, arrival_second = time_parser(arrival_time)
    departure_hour, departure_minute, departure_second = time_parser(
        departure_time)
    arrival_time = parse_date_time(
        arrival_hour, arrival_minute, arrival_second)
    departure_time = parse_date_time(
        departure_hour, departure_minute, departure_second)

    return type(arrival_time), type(departure_time)


def get_today_date_time(time_input):
    hour, minute, second = time_parser(time_input)
    convert_to_date_time = parse_date_time(hour, minute, second)
    get_datetime = parse_string_to_datetime(convert_to_date_time)
    return get_datetime


date = get_today_date_time('08:00:00')
# pt = parse_date_time(h, m, s)
# print(pt)
print(set_time('08:00:00', '12:00:00'))

# dramatiq_log.info('_____Now we are here_____', hot_desk_list)

data = [
    {'1L 106':
        {'section': '1L', 'number': '1L 106'},
     'isBeingSearched': False
     },
    {
        '1M 111':
        {'section': '1M', 'number': '1M 111'},
        'isBeingSearched': False
    }
]


SELECT DISTINCT hot_desk_ref_no FROM hot_desk_requests WHERE((arrival_time < '2019-09-12 08:00:00' AND
                                                              departure_time > '2019-09-12 09:00:00') OR(arrival_time > '2019-09-12 08:00:00' AND departure_time < '2019-09-12 09:00:00')
                                                             OR(arrival_time < '2019-09-12 08:00:00' AND departure_time between '2019-09-12 08:00:00' AND '2019-09-12 09:00:00')
                                                             OR(arrival_time < '2019-09-12 08:00:00' AND departure_time between '2019-09-12 08:00:00' AND '2019-09-12 09:00:00'
                                                                AND departure_time != '2019-09-12 08:00:00' AND arrival_time != '2019-09-12 09:00:00') OR(arrival_time > '2019-09-12 08:00:00'
                                                                                                                                                          AND departure_time > '2019-09-12 09:00:00' AND arrival_time between '2019-09-12 08:00:00' AND '2019-09-12 09:00:00'
                                                                                                                                                          AND arrival_time != '2019-09-12 09:00:00') OR(arrival_time > '2019-09-12 08:00:00' AND departure_time <= '2019-09-12 09:00:00')
                                                             OR(arrival_time='2019-09-12 08:00:00' AND departure_time >= '2019-09-12 09:00:00') OR(arrival_time='2019-09-12 08:00:00'
                                                                                                                                                   AND departure_time <= '2019-09-12 09:00:00')) AND(status='pending' OR status='approved')
