import os
import sys
import unittest

this_file_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.join(this_file_path, '../..')
sys.path.append(root_path)

from html2docx.onlaw_client.onlaw import Onlaw
from tests.testutils.util import async_test


class TestOnlaw(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.onlaw = Onlaw(client_id=os.environ['ONLAW_CLIENT_ID'],
                           client_secret=os.environ['ONLAW_CLIENT_SECRET'],
                           domain='auth-dev.onlaw.dk')

    @async_test
    async def test_get_token(self):
        await self.onlaw._get_token()
        access_token = Onlaw.api_server_token

        self.assertIsNotNone(access_token)
        self.assertIsInstance(access_token, str)
        # Just checks to see if the token has the three parts split by dots
        self.assertRegex(access_token, r'^.+\..+\..+$')


if __name__ == '__main__':
    unittest.main()
