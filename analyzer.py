import re
from scipy import stats
import os

def song_id(item):
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
    flags = (
        re.IGNORECASE |  # Match against upper and lower case with one case
        re.VERBOSE  # Match with comments
        )

    match = re.match(pattern, item, flags=flags)
    song_index = int(match.group("song_id"))

    return song_index

def artist_name(item):
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
    flags = (
        re.IGNORECASE |  # Match against upper and lower case with one case
        re.VERBOSE  # Match with comments
        )
        
    match = re.match(pattern, item, flags=flags)
    artist  = match.group("artist_name")
    artist = artist.replace('-',' ')
    return artist

def song_name(item):
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
    flags = (
        re.IGNORECASE |  # Match against upper and lower case with one case
        re.VERBOSE  # Match with comments
        )
        
    match = re.match(pattern, item, flags=flags)
    song = match.group("song_name")
    song = song.replace('-',' ')

    return song

def song_length(path,song,data):
    length_value = []
    for filename in os.listdir(path):
        song_file = path+ "/" + filename
        with open(song_file) as fp:
            all_data = fp.read()
        length_value.append(len(all_data))
    sorted_length = sorted(length_value)
    song_length = len(data)

    dimension = (stats.percentileofscore(sorted_length,song_length))/100
    return round(dimension,3)
