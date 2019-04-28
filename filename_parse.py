import os
import re

filelist = []
for filename in os.listdir(r"/home/gb2642/Tools-Project---Group-13/Lyrics"):
    filelist.append(filename)   
song_regex = []

for item in filelist:
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
             re.VERBOSE  # Match            
             )
    match = re.match(pattern, item, flags=flags)
    song_index = int(match.group("song_id"))
    song_regex.insert(song_index,match.groups()) 

print(song_regex)      
