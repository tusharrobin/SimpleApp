activate_this = '/home/tushar/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import unittest
import sample_app

class SampleAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = sample_app.app.test_client()

    def tearDown(self):
        pass

    def test_api(self):
        rv = self.app.get('/')
        assert b'Hello World!' in rv.data
if __name__ == '__main__':
    unittest.main()
