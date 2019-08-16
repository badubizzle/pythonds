def time_parser(time_input):
    hour, minutes = time_input.split(':')
    return int(hour), int(minutes)


def parse_date_time_to_string(hour, minutes):
    import datetime
    today = datetime.date.today()
    current_time = datetime.time(hour=hour, minute=minutes)
    return datetime.datetime.combine(today, current_time).strftime('%Y-%m-%d %H:%M')


def get_today_date_time(time_input):
    hour, minute = time_parser(time_input)
    convert_to_string_datetime = parse_date_time_to_string(
        hour, minute)
    return convert_to_string_datetime


def set_time(arrival_time, departure_time):
    arrival_time = get_today_date_time(arrival_time)
    departure_time = get_today_date_time(departure_time)
    return arrival_time, departure_time


print(parse_date_time_to_string(2019, 6, 10, 6))
