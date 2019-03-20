from unittest import TestLoader, TestSuite
import HtmlTestRunner
from tests.test import ApiTest 

example_tests = TestLoader().loadTestsFromTestCase(ApiTest)

suite = TestSuite([example_tests])

runner = HtmlTestRunner.HTMLTestRunner(output='reports',report_title='My Report')

runner.run(suite)