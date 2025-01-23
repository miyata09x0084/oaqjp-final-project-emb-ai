import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result_1 = emotion_detector("I'm happy this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

    def test_anger(self):
        result_2 = emotion_detector("I'm really angry about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

    def test_disgust(self):
        result_3 = emotion_detector("Just hearing this makes me sick")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

    def test_sadness(self):
        result_4 = emotion_detector("I'm very sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

    def test_fear(self):
        result_5 = emotion_detector("I'm really scared this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

    unittest.main()