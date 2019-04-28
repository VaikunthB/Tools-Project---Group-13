import os
import re
from statistics import median
path = r"/home/gb2642/Tools-Project---Group-13/Lyrics"
song_lengths = []
song_length_dic = {}
for filename in os.listdir(path):
    song_file = path+ r"/" + filename
    with open(song_file,encoding="latin1") as fp:
        data = fp.read().split()
        length_value = len(data)
        song_length_dic.update({filename: length_value})

import operator
sorted_d = sorted(song_length_dic.items(), key=operator.itemgetter(1))
number_of_songs = len(sorted_d)
song_length_dim = {}
length_values_sorted = sorted(song_length_dic.values())
from scipy import stats
for filename in os.listdir(path):
    dimension = (stats.percentileofscore(length_values_sorted, song_length_dic[filename])/100)
    song_length_dim.update({filename: dimension})
print(song_length_dim)
