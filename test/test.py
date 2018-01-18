import unittest
import requests

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.Url = 'http://qa-no-services.thebump.com/core/v1/hbib'
    
    def test_hbib_content(self):
        '''test hbib content'''
        r = requests.get(self.Url)
        print (r.json)
        self.assertEqual(r.status_code,200)
    
if __name__ == '__main__':
     unittest.main()
