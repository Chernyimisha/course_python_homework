# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам".


def group_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        # print(sorted_word)
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = [word]
        else:
            anagram_dict[sorted_word].append(word)
            print(anagram_dict)
    # print(anagram_dict)
    return list(anagram_dict.values())


input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
input_list_group = group_anagrams(input_list)

# print(input_list_group)


# details = {"Destination": "China",
#            "Nstionality": "Italian"}
# details["Age"] = [20, "Twenty"]
# print(details)

