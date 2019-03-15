import unittest
import htmlTestRunner
import requests
import sys
sys.path.append("..")
from commen.assertions import JsonResonseValidate
from commen.generate_data import Data

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.data = Data()
        # self.url = 'http://qa-no-services.thebump.com/core/v1/hbib'
        # self.jsonValidate = JsonResonseValidate('hbib.json')
        self.url, self.jsonSchema = self.data.get_test_data()
        self.jsonValidate = JsonResonseValidate(self.jsonSchema)
    
    def test_hbib_content(self):
        '''test hbib content'''
        r = requests.get(self.url)
        json_data = r.json()
        self.jsonValidate.assert_valid_schema(json_data) 
        self.assertEqual(r.status_code,200)
        
    
# if __name__ == '__main__':
#      unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports',report_title='My Report'))
