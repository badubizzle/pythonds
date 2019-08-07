def two_sum(array, target):
    dic = {}
    for index, number in enumerate(array):
        if number in dic:
            return dic[number], index
        else:
            dic[target - number] = index
    return None

# def two_sum(array):

#     for i in enumerate(array):
#         print(i)


two_sum([7, 2, 11, 15], 18)


# def two_sum(array, target):
#     dic = {}
#     for i, num in enumerate(array):
#         if num in dic:
#             return dic[num], i
#         else:
#             dic[target - num] = i
#     return None


def list_target(list, target):
    dict_mapper = {v: i for i, v in enumerate(list)}
    # create a dictionary that maps value to index
    sol_combinations = [[j, dict_mapper[target-x]]
                        for j, x in enumerate(list) if target-x in dict_mapper]
    # create a set of answers; make sure no key error by using 'if target-x in dict_mapper'
    answer = [x for x in sol_combinations if x[0] != x[1]]
    # Avoid self reference of indices. For instance list_target([1,2,0],2) returns [[0, 0], [1, 2], [2, 1]]; and [0,0] is a wrong answer
    return answer if answer else 'No solution found'


print(list_target([1, 2, 0], 2))
