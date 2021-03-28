

# Standard python library
import unittest

# local application imports
from checkurl import is_valid_signature, _extract

VALID_URL = ('http://someserver.com/?'
            'B02K_VERS=0003&B02K_TIMESTMP=50020181017141433899056&'
            'B02K_IDNBR=2512408990&B02K_STAMP=20010125140015123456&'
            'B02K_CUSTNAME=FIRST%20LAST&B02K_KEYVERS=0001&'
            'B02K_ALG=03&B02K_CUSTID=9984&B02K_CUSTTYPE=02&'
            'B02K_MAC=EBA959A76B87AE8996849E7C0C08D4AC44B053183BE12C0DAC2AD0C86F9F2542'
)
TEST_INPUT_SECRET = '&inputsecret&'

class Url_reading(unittest.TestCase):
    """docstring for Url_reading"""

    def test_extract_returns_dict_from_valid_url(self):
        self.assertIsInstance(_extract(VALID_URL),dict,
            "_extract returns a non dictionary object"
        )
    def test_extract_returns_all_10_items_from_valid_url(self):
        result = _extract(VALID_URL)
        keys = ['B02K_VERS','B02K_TIMESTMP','B02K_IDNBR','B02K_STAMP', 
        'B02K_CUSTNAME','B02K_KEYVERS','B02K_ALG','B02K_CUSTID', 
        'B02K_CUSTTYPE','B02K_MAC'
        ]
        self.assertEqual(len(result), 10,
            ("Looks like there's are not exactly 10 data items "
                "returned from this valid_url"
            )
        )
        for key in keys:
            self.assertIn(key, result, f'missing {key} in the given_url')


class Signature_verification(unittest.TestCase):
    """docstring for signature_verification"""

    def test_returns_false_with_bad_url(self):
        bad_url = 'http://badurl.com/?with&corrupted=data'
        self.assertFalse(is_valid_signature(bad_url, TEST_INPUT_SECRET))

    def test_output_is_error_url_from_unverified_signature(self):
        corrupted_data = ('http://example.com/?b02k_custname=mr%20malware&'
            'b02k_mac=267d3b81a9dcd937f3b46a17a57fc0ca2133373389336861142673a73fc17bc6')
        self.assertFalse(is_valid_signature(corrupted_data, TEST_INPUT_SECRET))

    def test_is_valid_signature_from_integral_signature(self):
        self.assertTrue(is_valid_signature(VALID_URL, TEST_INPUT_SECRET))


class Output_url(unittest.TestCase):
    """docstring for test_output_url"""

    def test_returns_error_url_from_non_verified_signature(self):
        self.fail("Finish the test")