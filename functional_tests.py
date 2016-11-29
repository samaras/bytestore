from selenium import webdriver 
import unittest

class NewVisitorTest(unittest.TestCase):

	def setup(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get("http://localhost:8083")

		# Check page title and header
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warinings='ignore')