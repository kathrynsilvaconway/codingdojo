# 1.
# def biggie_size(bigList):
#     for x in range(len(bigList)):
#         if bigList[x] > 0:
#             bigList[x] = 'big'
#     return bigList
# print(biggie_size(bigList = [3,-22,77,-5,12,-15]))

# 2.
# def count_positves(theList):
#     count = 0
#     for x in range(len(theList)):
#         if theList[x] < 0:
#             count += 1
#     theList[-1] = count
#     return theList
# print(count_positves(theList = [-3,22,-77,5,-12,15]))

# 3.
# def sum_total(totalList):
#     sum = 0
#     for x in range(len(totalList)):
#         sum += totalList[x]
#     return sum
# print(sum_total(totalList = [3,22,77,5,12,15]))
    
# 4.
# def average(totalList):
#     sum = 0
#     for x in range(len(totalList)):
#         sum += totalList[x]
#     ave = sum / len(totalList)
#     return ave
# print(average(totalList = [3,22,77,5,12,15]))

# 5.
# def length(theList):
#     count = len(theList)
#     return count
# print(length(theList = [3,22,77,5,12,15]))

# 6.
# def minimum(theList):
#     minimum = True
#     if len(theList) < 1:
#             minumum = False
#             return bool(minimum)
#     smallest = min(theList)
#     return smallest
# print(minimum(theList = [5,22,77,2,12,15]))

# 7.
# def maximum(theList):
#     maximum = True
#     if len(theList) < 1:
#             maximum = False
#             return bool(maximum)
#     largest = max(theList)
#     return largest
# print(maximum(theList = [5,22,77,2,12,15]))

# 8.
# def ultimate(theList):
#     ult_dict = {
#         'sumtotal': 0,
#         'average': 0,
#         'minimum': 0,
#         'maximum': 0,
#         'length': 0
#         }
#     for x in range(len(theList)):
#         ult_dict['sumtotal'] += theList[x]
#         ult_dict['average'] = ult_dict['sumtotal'] / len(theList)
#         ult_dict['minimum'] = min(theList)
#         ult_dict['maximum'] = max(theList)
#         ult_dict['length'] = len(theList)
#     return ult_dict
# print(ultimate(theList = [3,22,77,5,12,15]))

# 9.
# def reverse(theList):
#     theList.reverse()
#     return theList
# print(reverse(theList = [3,22,77,5,12,15]))





    



