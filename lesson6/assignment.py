def two_sum(array, target):
    dic = {}
    for i, num in enumerate(array):
        import pdb
        pdb.set_trace()
        if num in dic:
            return dic[num], i
        else:
            dic[target - num] = i
    return None


# def two_sum(array):

#     for i in enumerate(array):
#         print(i)


two_sum([7, 2, 11, 15], 18)
