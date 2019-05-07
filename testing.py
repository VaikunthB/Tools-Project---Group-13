import unittest
import main
import analyzer

class TestMain(unittest.TestCase):

    def test_main(self):
        path = 'Lyrics'
        self.assertIsInstance(main.main(path), str)

    def test_path_error(self):
        with self.assertRaises(TypeError):
            main.main()

class TestClassMethods(unittest.TestCase):

    def test_song_id(self):
        self.assertEqual(analyzer.song_id('003~Jeff-Beck~All-Shook-Up.txt'), 3)

    def test_song_artist(self):
        self.assertEqual(analyzer.artist_name('003~Jeff-Beck~All-Shook-Up.txt'), 'Jeff Beck')

    def test_song_title(self):
        self.assertEqual(analyzer.song_name('003~Jeff-Beck~All-Shook-Up.txt'), 'All Shook Up')

    def test_kid_safe(self):
        self.assertEqual(analyzer.child_friend('I like flowers. This is a child frinedly song'), 1)
        self.assertEqual(analyzer.child_friend('Fuck you motherfucker, bitches whore moher fuck fuck you fucking fucker fuck whore bitch'), 0)

    def test_love(self):
        self.assertEqual(analyzer.love('You are love love beautiful graceful darling angel joy'), 1)
        self.assertEqual(analyzer.love('I want to move to University and chill on the beach'), 0)

    def test_mood(self):
            self.assertEqual(analyzer.mood('I am so happy and cheerful and energetic'), 0.9)

    def test_length(self): 
            self.assertEqual(analyzer.song_length('I am small'), 0)

    if __unit__ == '__main__': 
            unittest.main()


