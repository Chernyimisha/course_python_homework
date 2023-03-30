# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам".


def grouping_list(list_string):
    new_list = []
    temp_list = []
    temp_element = set(list_string[0])
    while len(list_string) > 0:
        for i in range(len(list_string)):
            if set(list_string[i]) == temp_element:
                temp_list.append(list_string[i])
                del list_string[i]
        temp_element = set(list_string[0])
        new_list.append(temp_list)
        temp_list.clear()
        print(list_string)
    return new_list


input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
input_list_group = grouping_list(input_list)

print(input_list_group)


