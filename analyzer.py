import re
from scipy import stats
import file_extractor as fe
import stopwords as sw

def bad_words():
    arrBad = ['nigga','shit','fuck','bitch','niggas','ass','fucking','niggaz','bitches','sex','dick','pussy','fucked','motherfucker','fuckin','lust','bum','motherfuckers',
            'cock','shite','butt','whore','motherfucking','piss','cum','b****','***','****','*****','n****']
    return arrBad

def bad_lengths(folder_data):
    length_value = []

    for item in folder_data:
        item_split = item.split()
        count = len(list(set(item_split) & set(bad_words())))
        length_value.append(count)
    length_value.sort()

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

def song_length(data,sorted_length):
    song_length = len(data)
    dimension = (stats.percentileofscore(sorted_length,song_length))/100
    return round(dimension,3)

def child_friend(data,bad_avg):
    data.lower()
    split_data = data.split()
    song_length = len(list(set(split_data) & set(bad_words())))

    if song_length == 0:
        return 1

    else:
        dimension = (stats.percentileofscore(bad_avg,song_length))/100
        return (1-round(dimension,3))

def mood():
    gggr

def love(data,love_avg):
    data.lower()
    split_data = data.split()

    common_elements = (set(split_data) & set(sw.love_words()))
    love_length = len(common_elements)

    if love_length == 0:
        return 0

    else:
        dimension = (stats.percentileofscore(love_avg,love_length))/100
        return round(dimension,3)
    
    

def complexity(data,complex_avg):
    data.lower()
    item_split = data.split()

    real_words = (set(item_split) - (set(item_split) & set(sw.stop())))

    no_realwords = len(real_words)
    if len(data) == 0:
        return 0

    else:
        dimension = (stats.percentileofscore(complex_avg,no_realwords))/100
        return round(dimension,3)









