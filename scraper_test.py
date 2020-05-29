"""Using unittest to test scrape file"""
import unittest
import scrape

class webTest(unittest.TestCase): 
    def test_headline (self):
        cnn_headline = scrape.Scraper("https://www.cnn.com/australia", "//img[@class='media__image media__image--responsive']", "//h3[@data-analytics='dummy_class']")
        cnn_headline.scraper()
        self.assertEqual(cnn_headline.print_headline(), "None")
if __name__ == '__main__':
    unittest.main()
