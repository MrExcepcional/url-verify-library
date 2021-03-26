

# Standard python library
import unittest

# local application imports
from checkurl import valid_signature, extract


class Url_reading(unittest.TestCase):
    """docstring for Url_reading"""
    def test_extract_returns_all_10_items_from_valid_url(self):
        valid_url = 'http://someserver.com/?B02K_VERS=0003&B02K_TIMESTMP=50020181017141433899056&B02K_IDNBR=2512408990&B02K_STAMP=20010125140015123456&B02K_CUSTNAME=FIRST%20LAST&B02K_KEYVERS=0001&B02K_ALG=03&B02K_CUSTID=9984&B02K_CUSTTYPE=02&B02K_MAC=EBA959A76B87AE8996849E7C0C08D4AC44B053183BE12C0DAC2AD0C86F9F2542'
        self.assertEqual(len(extract(valid_url)), 10)

class Signature_verification(unittest.TestCase):
    """docstring for signature_verification"""

    def test_output_is_error_url_from_unverified_signature(self):
        corrupted_data = 'http://example.com/?b02k_custname=mrmalware&b02k_mac=267d3b81a9dcd937f3b46a17a57fc0ca2133373389336861142673a73fc17bc6'
        self.assertFalse(valid_signature(corrupted_data))

    def test_a_valid_signature(self):
        normal_data = ''
        self.assertTrue(valid_signature(normal_data))
