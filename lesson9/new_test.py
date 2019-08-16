
# from .test import get_date_time


def get_date_time(hour, minutes, seconds):
    import datetime
    today = datetime.date.today()
    current_time = datetime.time(hour=hour, minute=minutes)
    return datetime.datetime.combine(today, current_time).strftime('%Y:%m:%d %H:%M:%S')


def time_parser(time_input):
    hour, minutes, seconds = time_input.split(':')
    return int(hour), int(minutes), int(seconds)


def set_time(arrival_time, departure_time):
    from datetime import datetime
    arrival_hour, arrival_minute, arrival_second = time_parser(arrival_time)
    departure_hour, departure_minute, departure_second = time_parser(
        departure_time)
    arrival_time = get_date_time(
        arrival_hour, arrival_minute, arrival_second)
    departure_time = get_date_time(
        departure_hour, departure_minute, departure_second)
    return arrival_time, departure_time


def parse_string_time(string_time_input):
    from datetime import datetime
    coverted_date_time = datetime.strptime(
        string_time_input, '%Y:%m:%d %H:%M:%S')
    return type(coverted_date_time)


print(set_time('08:00:00', '18:00:00'))
print(parse_string_time('2019:08:27 08:00:00'))
