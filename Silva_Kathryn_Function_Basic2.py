
# 1.
# def countdown():
#     count_start = int(input("Enter a number to count dowm from: "))
#     countdown_list = []
#     for x in range(count_start, 0, -1):
#         countdown_list.append(x)
#     return countdown_list
# print(countdown())

# 2.
# def print_and_return(list = []):
#     print(list[0])
#     return list[1]
# answer = print_and_return(list =[3,8])
# print(answer)

# 3.
# def first_plus_length(list = []):
#     return list[0] + len(list)
# print(first_plus_length(list = [3,22,77,5,12,15]))

# # 4.
def greater_than_second(myList=[]):
    new_list = []
    for x in myList:
        if x > myList[1]:
            new_list.append(x)
        if len(new_list) > 2:
            greater_than_second = False
        if len(new_list) < 2:
            greater_than_second = True
    print(bool(greater_than_second))
    print(len(new_list))
    return new_list


print(greater_than_second(myList=[3, 22, 77, 5, 12, 15]))

# 5.
# def length_and_value(a,b):
#     myList = [b]
#     for b in myList:
#         if a > len(myList):
#             myList.append(b)
#     return myList
# print(length_and_value(6,10))
