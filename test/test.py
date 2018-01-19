import unittest
import HtmlTestRunner
import requests
import json
import sys
sys.path.append("..")
from commen.assertions import assert_valid_schema
# from commen.assertions import JsonResonseValidate

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.Url = 'http://qa-no-services.thebump.com/core/v1/hbib'
        # self.jsonValidate = JsonResonseValidate()
    
    def test_hbib_content(self):
        '''test hbib content'''
        r = requests.get(self.Url)
        json_data = r.json()
        assert_valid_schema(json_data, 'hbib.json') 
        self.assertEqual(r.status_code,200)
        
    
if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
