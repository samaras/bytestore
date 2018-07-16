from django.test import LiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):

	def setup(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

class NewVisitorTest(unittest.TestCase):

	def setup(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get(self.live_server_url)

		# Check page title and header
		self.assertIn('Byte', self.browser.title)
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warinings='ignore')
