import os
import sys
import unittest

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(this_file_path + '/..'))
from onlaw_api_client.client import Onlaw


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_given_fake_credentials_when_instatiate_client_then_validate_object_created(self):
        onlaw_client: Onlaw = Onlaw('my_id', 'my_secret')
        self.assertEqual(onlaw_client._token, '')


if __name__ == '__main__':
    unittest.main()
