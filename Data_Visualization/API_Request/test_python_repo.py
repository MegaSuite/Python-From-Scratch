import unittest
import requests

class TestPythonRepo(unittest.TestCase):
    def test_python_repo(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        r= requests.get(url)
        self.assertEqual(str(r.status_code), '200')


unittest.main()