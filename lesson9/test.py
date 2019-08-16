# import datetime


# today = date.today()
# dates = str(today) + ' 18:00:00'
# # print("Today's date:", type(dates))
# # print(type(today))

# print(type(datetime.datetime.now()))


# def alphabet_position(text):
# alphabeths = {
#      "a": 1,
#       "b": 2,
#      "c": 3,
#         "d": 4,
#         "e": 5,
#         "f": 6,
#         "g": 7,
#         "h": 8,
#         "i": 9,
#         "j": 10,
#         "k": 11,
#         "l": 12,
#         "m": 13,
#         "n": 14,
#         "o": 15,
#         "p": 16,
#         "q": 17,
#         "r": 18,
#         "s": 19,
#         "t": 20,
#         "u": 21,
#         "v": 22,
#         "w": 23,
#         "x": 24,
#         "y": 25,
#         "z": 26
#      }

#  lower_case = text.lower()

#   alphabet_numbers = []
#    for value in lower_case:
#         if value not in alphabeths:
#             pass
#         else:
#             alphabet_numbers.append(str(alphabeths[value]))

#     return '  '.join(alphabet_numbers)


# print(alphabet_position("The sunset sets at twelve o' clock."))
# alphabeths = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
#     "e": 5,
#     "f": 6,
#     "g": 7,
#     "h": 8,
#     "i": 9,
#     "j": 10,
#     "k": 11,
#     "l": 12,
#     "m": 13,
#     "n": 14,
#     "o": 15,
#     "p": 16,
#     "q": 17,
#     "r": 18,
#     "s": 19,
#     "t": 20,
#     "u": 21,
#     "v": 22,
#     "w": 23,
#     "x": 24,
#     "y": 25,
#     "z": 26
# }

# # print(alphabeths.items())
# pp = next(iter(alphabeths.items()))
# print(pp)

# import datetime
# yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
# new_period = yesterday.replace(hour=23, minute=30).strftime('%Y-%m-%d')
# print(new_period)
# import datetime


# # print()


# from main import dramatiq_log


# def time_parser(time_input):
#     hour, minutes, seconds = time_input.split(':')
#     return int(hour), int(minutes), int(seconds)


# def get_date_time(hour, minutes, seconds):
#     today = datetime.date.today()
#     current_time = datetime.time(hour=hour, minute=minutes)
#     return datetime.datetime.combine(today, current_time).strftime('%Y-%m-%d %H:%M')


# dramatiq_log = dramatiq.logging.get_logger(__name__)
# dramatiq_log.info('_____Now we are here_____', hot_desks)


# print(date_time_formatter('08:00:00'))


# def is_departure_less_than_arrival():


# arrival_time = get_date_time(8, 30)
# departure_time = get_date_time(18, 00)
# tt = datetime.strptime(arrival_time, '%Y-%m-%d')

# def is_departure_less_than_arrival():
#     if departure_time < arrival_time:
#         return False
#     return True


# print(is_departure_less_than_arrival())
# print(departure_time - arrival_time)
# print(arrival_time - departure_time)


# arr = [' 1L 103 ', '1L 104', '1L 105', '1L 106', '1L 107', '1L 108', '1L 109', '1L 110', '1M 111', '1M 112', '1M 113', '1M 114',
#        '1M 115', '1M 116', '1M 117', '1M 118', '1N 119', '1N 120', '1N 121', '1N 122', '1N 123', '1N 124', '1N 125', '1N 126']

# hot_desk_list_ = [x.strip(' ') for x in arr]

# print(arr)
# print(hot_desk_list_)

# arr1 = [{'1 s t   f l o o r': [' 1L 103', ' 1L 104', ' 1L 105', ' 1L 106', ' 1L 107', ' 1L 108', ' 1L 109', ' 1L 110', ' 1M 111', ' 1M 112', ' 1M 113',
#                                ' 1M 114', ' 1M 115', ' 1M 116', ' 1M 117', ' 1M 118', ' 1N 119', ' 1N 120', ' 1N 121', ' 1N 122', ' 1N 123', ' 1N 124', ' 1N 125', ' 1N 126']}]

# pending_hot_desk_refs = ['1L 103', '1L 104',
#                          '1L 105', '1L 106', '1L 107', '1L 108', ]


# def filter_hotdesk(hot_desk_list):
#     hot_desk_list_ = []
#     for each in hot_desk_list:
#         pp = next(iter(each.items()))
#         import pdb
#         pdb.set_trace()
#         hot_desk_list_ = pp[1]
#         key = pp[0]
#         hot_desk_list_ = [x.strip(' ') for x in hot_desk_list_]
#         non_requested_desks = [
#             obj for obj in hot_desk_list_ if obj not in pending_hot_desk_refs
#         ]
#         each[key] = non_requested_desks
#     return hot_desk_list


# print(filter_hotdesk(arr1))


# def time_parser(time_input):
#     import datetime
#     hour, minutes, seconds = time_input.split(':')
#     return int(hour), int(minutes), int(seconds)


# def parse_date_time(hour, minutes, seconds):
#     import datetime
#     today = datetime.date.today()
#     current_time = datetime.time(hour=hour, minute=minutes)
#     return datetime.datetime.combine(today, current_time).strftime('%Y:%m:%d %H:%M:%S')


# def parse_string_time(string_time_input):
#     from datetime import datetime

#     coverted_date_time = datetime.strptime(
#         string_time_input, '%Y:%m:%d %H:%M')

#     return coverted_date_time


# def set_time(arrival_time, departure_time):
#     arrival_hour, arrival_minute, arrival_second = time_parser(arrival_time)
#     departure_hour, departure_minute, departure_second = time_parser(
#         departure_time)
#     arrival_time = parse_date_time(
#         arrival_hour, arrival_minute, arrival_second)
#     departure_time = parse_date_time(
#         departure_hour, departure_minute, departure_second)

#     cache.set('arrival_time', arrival_time, timeout=50)
#     cache.set('departure_time', departure_time, timeout=50)


# print(parse_string_time('2019:08:28 08:00'))

# start_time
# end_time
# status
# hotdesk


arr = [2, 4, 5]


def return_one(arr):
    for ar in arr:
        import pdb
        pdb.set_trace()
        if arr == 1:
            return False


print(return_one(arr))
