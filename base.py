

import unittest
import os

import checkurl

TEST_INPUT_SECRET = 'inputsecret'
TEST_OUTPUT_SECRET = 'outputsecret'
VALID_URL = ('http://someserver.com/?'
            'B02K_VERS=0003&B02K_TIMESTMP=50020181017141433899056&'
            'B02K_IDNBR=2512408990&B02K_STAMP=20010125140015123456&'
            'B02K_CUSTNAME=FIRST%20LAST&B02K_KEYVERS=0001&'
            'B02K_ALG=03&B02K_CUSTID=9984&B02K_CUSTTYPE=02&'
            'B02K_MAC=EBA959A76B87AE8996849E7C0C08D4AC44B053183BE12C0DAC2AD0C86F9F2542'
)

class LibraryTest(unittest.TestCase):
    """docstring for LibraryTest"""
    def setUp(self):
        self.checkurl = checkurl
        self.checkurl.INPUT_SECRET = TEST_INPUT_SECRET
        self.checkurl.OUTPUT_SECRET = TEST_OUTPUT_SECRET
        self.valid_url = VALID_URL