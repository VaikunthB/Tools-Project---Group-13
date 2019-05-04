import os

def main(lyrics_folder):

    filelist = []

    for filename in os.listdir(lyrics_folder):
        filelist.append(filename)
    filelist.sort()
    print(filelist)

    for item in filelist:
        with open(item,encoding="latin1") as fp:
            data = fp.read()



if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser('Music Lyrics Classification')
    parser.add_argument('lyrics_folder', help = 'Enter the absolute path of the Lyrics folder')

    args = parser.parse_args()
    main(args.lyrics_folder)
