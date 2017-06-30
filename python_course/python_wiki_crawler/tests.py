import unittest
import wiki_crawling


class TestContinueCrawlFunction(unittest.TestCase):
    def test_first_fail_in_continue_crawl(self):
        self.target_url = 'https://en.wikipedia.org/wiki/Philosophy'
        self.search_history = ['https://en.wikipedia.org/wiki/Ethics',
                               'https://en.wikipedia.org/wiki/Applied_ethics',
                               'https://en.wikipedia.org/wiki/Philosophy']
        self.assertFalse(wiki_crawling.continue_crawl(self.search_history, self.target_url))

    def test_second_fail_in_continue_crawl(self):
        self.target_url = 'https://en.wikipedia.org/wiki/Philosophy'
        self.search_history = ['https://en.wikipedia.org/wiki/Business_ethics',
                               'https://en.wikipedia.org/wiki/Applied_ethics', 'https://en.wikipedia.org/wiki/Ethics']
        self.search_history *= 10
        self.assertFalse(wiki_crawling.continue_crawl(self.search_history, self.target_url))

    def test_third_fail_in_continue_crawl(self):
        self.target_url = 'https://en.wikipedia.org/wiki/Philosophy'
        self.search_history = ['https://en.wikipedia.org/wiki/Business_ethics', 'https://en.wikipedia.org/wiki/Pebbles',
                               'https://en.wikipedia.org/wiki/Dirt',
                               'https://en.wikipedia.org/wiki/Mud', 'https://en.wikipedia.org/wiki/Business_ethics']
        self.assertFalse(wiki_crawling.continue_crawl(self.search_history, self.target_url))

    def test_else_pass_in_continue_crawl(self):
        self.target_url = 'https://en.wikipedia.org/wiki/Philosophy'
        self.search_history = ['https://en.wikipedia.org/wiki/Business_ethics',
                               'https://en.wikipedia.org/wiki/Applied_ethics',
                               'https://en.wikipedia.org/wiki/Business_standards']
        self.assertTrue(wiki_crawling.continue_crawl(self.search_history, self.target_url))


class TestFindFirstLink(unittest.TestCase):
    def test_returns_first_link(self):
        self.assertIsInstance(wiki_crawling.find_first_link('https://en.wikipedia.org/wiki/Applied_ethics'), str)

if __name__ == '__main__':
    unittest.main()
