import os
import analyzer
import json
import file_extractor as fe


def main(lyrics_folder):

    filelist = []
    length_value = []

    for filename in os.listdir(lyrics_folder):
        filelist.append(filename)

    filelist.sort()
    final_list = []

    for item in filelist[0:10]:
        path = lyrics_folder + "/" + item
        data = fe.extractor(path)
            
        song_id = analyzer.song_id(item)
        artist_name = analyzer.artist_name(item)
        song_name = analyzer.song_name(item)
        song_length = analyzer.song_length(data,lyrics_folder)

        song_attributes = {
               'id' : song_id,
               'artist': artist_name,
               'title':song_name,
               'length':song_length
               }
        final_list.append(song_attributes)
    json_input = {'characterizations' : final_list}

    print(json.dumps(json_input, indent = 3))


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser('Music Lyrics Classification')
    parser.add_argument('lyrics_folder', help = 'Enter the absolute path of the Lyrics folder')

    args = parser.parse_args()
    main(args.lyrics_folder)
