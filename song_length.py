import os
import re
from statistics import median
path = "/home/gb2642/Tools-Project---Group-13/Lyrics"
song_lengths = []
song_length_dic = {}
for filename in os.listdir(path):
    song_file = path+ r"/" + filename
    with open(song_file,encoding="utf8") as fp:
        data = fp.read().split()
        length_value = len(data)
        song_length_dic.update({ 
            filename: length_value
            })
print(song_length_dic)
