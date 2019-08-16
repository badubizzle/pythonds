hot_desk_list = [{'1 s t   f l o o r': ['1G 66', '1L 103', '1L 104', '1L 105', '1L 106', '1L 107', '1L 108', '1L 109', '1L 110', '1M 111', '1M 112', '1M 113',
                                        '1M 114', '1M 115', '1M 116', '1M 117', '1M 118', '1N 119', '1N 120', '1N 121', '1N 122', '1N 123', '1N 124', '1N 125', '1N 126']}]


def get_non_requested_hotdesks(hot_desk_list):
    """
    get the hotdesks that have not been requested

    Args:
        hot_desk_list (list): list of all the hotdesk

    Returns:
        list: list of hotdesks that have not been requested
    """

    unavailable_hotdesks = ['1L 106', '1M 111']

    hot_desk_list_ = []
    for each in hot_desk_list:
        pp = next(iter(each.items()))
        hot_desk_list_ = pp[1]
        key = pp[0]
        hot_desk_list_ = [x.strip(' ') for x in hot_desk_list_]
        non_requested_desks = [
            obj for obj in hot_desk_list_ if obj not in unavailable_hotdesks
        ]
        each[key] = non_requested_desks
    return hot_desk_list


print(get_non_requested_hotdesks(hot_desk_list))
