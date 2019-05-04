import re
from scipy import stats
import os
import file_extractor as fe


def folder_lengths(lyrics_folder):
    length_value = []
    for filename in os.listdir(lyrics_folder):
        song_file = lyrics_folder + "/" + filename
        length_value.append(len(fe.extractor(song_file)))
    return length_value

def pattern():
    pattern = r'''
        ^
        (?P<song_id>\d+)
        [~]{1}
        (?P<artist_name>\S+)
        [~]{1}
        (?P<song_name>\S+)
        [.]{1}
        (\w{3})
        $
        '''
    return pattern

def flags():
    flags = (
        re.IGNORECASE |  # Match against upper and lower case with one case
        re.VERBOSE  # Match with comments
        )

    return flags
def song_id(item):
    
    match = re.match(pattern(), item, flags=flags())
    song_index = int(match.group("song_id"))

    return song_index

def artist_name(item):
        
    match = re.match(pattern(), item, flags=flags())
    artist  = match.group("artist_name")
    artist = artist.replace('-',' ')
    return artist

def song_name(item):
            
    match = re.match(pattern(), item, flags=flags())
    song = match.group("song_name")
    song = song.replace('-',' ')

    return song

def song_length(data,lyrics_folder):
    sorted_length = sorted(folder_lengths(lyrics_folder))
    song_length = len(data)

    dimension = (stats.percentileofscore(sorted_length,song_length))/100
    return round(dimension,3)

def child_friend(path,song,data):
    uhihbib
