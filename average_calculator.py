from stopwords import stop
from stopwords import love_words
import collections
def complexity(folder_data):
    complex_len = []

    for item in folder_data:
        item.lower()
        item_split = item.split()
        real_words = (set(item_split) - (set(item_split) & set(stop())))
        
        complex_len.append(len(real_words))

    return complex_len

def song_length(folder_data):
    sorted_length = []

    for item in folder_data:
        sorted_length.append(len(item))
    sorted_length.sort()

    return sorted_length

def love(folder_data):
    love_length = []

    for item in folder_data:
        item.lower()
        split_data = item.split()
        

        common_elements = (set(split_data) & set(love_words()))
        love_length.append(len(common_elements))

    love_length.sort()

    return love_length

