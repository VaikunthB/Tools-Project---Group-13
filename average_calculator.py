from stopwords import stop
import collections
def complexity(folder_data):
    complex_len = []

    for item in folder_data:
        item_split = item.split()
        real_words = []
        for word in item_split:
            if word  not in stop():
                real_words.append(word)
        no_realwords = len(collections.Counter(real_words))
        complex_len.append(no_realwords)

    return complex_len

def song_length(folder_data):
    sorted_length = []

    for item in folder_data:
        sorted_length.append(len(item))
    sorted_length.sort()

    return sorted_length
