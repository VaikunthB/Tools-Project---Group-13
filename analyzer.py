import re


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

