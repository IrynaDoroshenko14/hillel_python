string_input = input("Please, enter string: ")


def get_word_count(string):
    word_list = string.split(" ")
    count = len(word_list)
    return count


word_count = get_word_count(string_input)
print(word_count)
print(len(string_input))
