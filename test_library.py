

# Standard python library
import unittest

# local application imports
from checkurl import verify_signature, ERROR_URL


class signature_verification(unittest.TestCase):
    """docstring for signature_verification"""

    def test_output_is_an_error_url_from_unverified_signature(self):
        bad_url_signature = 'http://example.com/?b02k_mac=invalidsignature'
        self.assertEqual(ERROR_URL, verify_signature(bad_url_signature))