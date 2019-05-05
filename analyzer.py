import re
from scipy import stats
import os
import file_extractor as fe

def bad_words():
    arrBad = [
            '2g1c',
            '2 girls 1 cup',
            'acrotomophilia',
            'anal',
            'anilingus',
            'anus',
            'arsehole',
            'ass',
            'asshole',
            'assmunch',
            'auto erotic',
            'autoerotic',
            'babeland',
            'baby batter',
            'ball gag',
            'ball gravy',
            'ball kicking',
            'ball licking',
            'ball sack',
            'ball sucking',
            'bangbros',
            'bareback',
            'barely legal',
            'barenaked',
            'bastardo',
            'bastinado',
            'bbw',
            'bdsm',
            'beaver cleaver',
            'beaver lips',
            'bestiality',
            'bi curious',
            'big black',
            'big breasts',
            'big knockers',
            'big tits',
            'bimbos',
            'birdlock',
            'bitch',
            'black cock',
            'blonde action',
            'blonde on blonde action',
            'blow j',
            'blow your l',
            'blue waffle',
            'blumpkin',
            'bollocks',
            'bondage',
            'boner',
            'boob',
    'boobs',
    'booty call',
    'brown showers',
    'brunette action',
    'bukkake',
    'bulldyke',
    'bullet vibe',
    'bung hole',
    'bunghole',
    'busty',
    'butt',
    'buttcheeks',
    'butthole',
    'camel toe',
    'camgirl',
    'camslut',
    'camwhore',
    'carpet muncher',
    'carpetmuncher',
    'chocolate rosebuds',
    'circlejerk',
    'cleveland steamer',
    'clit',
    'clitoris',
    'clover clamps',
    'clusterfuck',
    'cock',
    'cocks',
    'coprolagnia',
    'coprophilia',
    'cornhole',
    'cum',
    'cumming',
    'cunnilingus',
    'cunt',
    'darkie',
    'date rape',
    'daterape',
    'deep throat',
    'deepthroat',
    'dick',
    'dildo',
    'dirty pillows',
    'dirty sanchez',
    'dog style',
    'doggie style',
    'doggiestyle',
    'doggy style',
    'doggystyle',
    'dolcett',
    'domination',
    'dominatrix',
    'dommes',
    'donkey punch',
    'double dong',
    'double penetration',
    'dp action',
    'eat my ass',
    'ecchi',
    'ejaculation',
    'erotic',
    'erotism',
    'escort',
    'ethical slut',
    'eunuch',
    'faggot',
    'fecal',
    'felch',
    'fellatio',
    'feltch',
    'female squirting',
    'femdom',
    'figging',
    'fingering',
    'fisting',
    'foot fetish',
    'footjob',
    'frotting',
    'fuck',
    'fucking',
    'fuck buttons',
    'fudge packer',
    'fudgepacker',
    'futanari',
    'g-spot',
    'gang bang',
    'gay sex',
    'genitals',
    'giant cock',
    'girl on',
    'girl on top',
    'girls gone wild',
    'goatcx',
    'goatse',
    'gokkun',
    'golden shower',
    'goo girl',
    'goodpoop',
    'goregasm',
    'grope',
    'group sex',
    'guro',
    'hand job',
    'handjob',
    'hard core',
    'hardcore',
    'hentai',
    'homoerotic',
    'honkey',
    'hooker',
    'hot chick',
    'how to kill',
    'how to murder',
    'huge fat',
    'humping',
    'incest',
    'intercourse',
    'jack off',
    'jail bait',
    'jailbait',
    'jerk off',
    'jigaboo',
    'jiggaboo',
    'jiggerboo',
    'jizz',
    'juggs',
    'kike',
    'kinbaku',
    'kinkster',
    'kinky',
    'knobbing',
    'leather restraint',
    'leather straight jacket',
    'lemon party',
    'lolita',
    'lovemaking',
    'make me come',
    'male squirting',
    'masturbate',
    'menage a trois',
    'milf',
    'missionary position',
    'motherfucker',
    'mound of venus',
    'mr hands',
    'muff diver',
    'muffdiving',
    'nambla',
    'nawashi',
    'negro',
    'neonazi',
    'nig nog',
    'nigga',
    'nigger',
    'nimphomania',
    'nipple',
    'nipples',
    'nsfw images',
    'nude',
    'nudity',
    'nympho',
    'nymphomania',
    'octopussy',
    'omorashi',
    'one cup two girls',
    'one guy one jar',
    'orgasm',
    'orgy',
    'paedophile',
    'panties',
    'panty',
    'pedobear',
    'pedophile',
    'pegging',
    'penis',
    'phone sex',
    'piece of shit',
    'piss pig',
    'pissing',
    'pisspig',
    'playboy',
    'pleasure chest',
    'pole smoker',
    'ponyplay',
    'poof',
    'poop chute',
    'poopchute',
    'porn',
    'porno',
    'pornography',
    'prince albert piercing',
    'pthc',
    'pubes',
    'pussy',
    'queaf',
    'raghead',
    'raging boner',
    'rape',
    'raping',
    'rapist',
    'rectum',
    'reverse cowgirl',
    'rimjob',
    'rimming',
    'rosy palm',
    'rosy palm and her 5 sisters',
    'rusty trombone',
    's&m',
    'sadism',
    'scat',
    'schlong',
    'scissoring',
    'semen',
    'sex',
    'sexo',
    'sexy',
    'shaved beaver',
    'shaved pussy',
    'shemale',
    'shibari',
    'shit',
    'shota',
    'shrimping',
    'slanteye',
    'slut',
    'smut',
    'snatch',
    'snowballing',
    'sodomize',
    'sodomy',
    'spic',
    'spooge',
    'spread legs',
    'strap on',
    'strapon',
    'strappado',
    'strip club',
    'style doggy',
    'suck',
    'sucks',
    'suicide girls',
    'sultry women',
    'swastika',
    'swinger',
    'tainted love',
    'taste my',
    'tea bagging',
    'threesome',
    'throating',
    'tied up',
    'tight white',
    'tit',
    'tits',
    'titties',
    'titty',
    'tongue in a',
    'topless',
    'tosser',
    'towelhead',
    'tranny',
    'tribadism',
    'tub girl',
    'tubgirl',
    'tushy',
    'twat',
    'twink',
    'twinkie',
    'two girls one cup',
    'undressing',
    'upskirt',
    'urethra play',
    'urophilia',
    'vagina',
    'venus mound',
    'vibrator',
    'violet blue',
    'violet wand',
    'vorarephilia',
    'voyeur',
    'vulva',
    'wank',
    'wet dream',
    'wetback',
    'white power',
    'women rapping',
    'wrapping men',
    'wrinkled starfish',
    'xx',
    'xxx',
    'yaoi',
    'yellow showers',
    'yiffy',
    'zoophilia']
    return arrBad

def bad_lengths(lyrics_folder):
    length_value = []

    for filename in os.listdir(lyrics_folder):
        song_file = lyrics_folder + "/" +filename
        data = fe.extractor(song_file)
        count = 0
        for word in data:
            if word in bad_words():
                count += 1
        length_value.append(count)
        length_value.sort()

        return length_value

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

def child_friend(data,lyrics_folder):
    count = 0
    for word in data:
        if word in bad_words():
            count += 1
    song_length = count

    dimension = (stats.percentileofscore(bad_lengths(lyrics_folder),song_length))/100
    return round(dimension,3)
