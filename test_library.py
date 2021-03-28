#!/usr/bin/python3.9

# Standard python library
from urllib.error import URLError

# local application imports
from base import LibraryTest


class Url_reading(LibraryTest):
    """docstring for Url_reading"""

    def test_extract_returns_dict_from_valid_url(self):
        self.assertIsInstance(self.checkurl._extract(self.valid_url),dict,
            "_extract returns a non dictionary object"
        )
    def test_extract_returns_all_10_items_from_valid_url(self):
        result = self.checkurl._extract(self.valid_url)
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

    def test_extract_supports_non_ascii_letters(self):
        windows_1252_encoded_url = ('http://someserver.com/?'
            'B02K_VERS=0003&B02K_TIMESTMP=50020181017141433899056&'
            'B02K_IDNBR=2512408990&B02K_STAMP=20010125140015123456&'
            'B02K_CUSTNAME=V%C4IN%D6%20M%C4KI&B02K_KEYVERS=0001&'
            'B02K_ALG=03&B02K_CUSTID=9984&B02K_CUSTTYPE=02&'
            'B02K_MAC=EBA959A76B87AE8996849E7C0C08D4AC44B053183BE12C0DAC2AD0C86F9F2542'
        )
        result = self.checkurl._extract(windows_1252_encoded_url)
        self.assertEqual('VÄINÖ MÄKI', result['B02K_CUSTNAME'][0])


class Signature_verification(LibraryTest):
    """docstring for signature_verification"""

    def test_is_valid_signature_returns_false_with_bad_url(self):
        bad_url = 'http://badurl.com/?with&strage=data'
        self.assertFalse(self.checkurl.is_valid_signature(bad_url))

    def test_output_is_error_url_from_unverified_signature(self):
        corrupted_data = ('http://example.com/?b02k_custname=mr%20malware&'
            'b02k_mac=267d3b81a9dcd937f3b46a17a57fc0ca2133373389336861142673a73fc17bc6')
        self.assertFalse(self.checkurl.is_valid_signature(corrupted_data))

    def test_is_valid_signature_from_integral_signature(self):
        self.assertTrue(self.checkurl.is_valid_signature(self.valid_url))


class Output_url(LibraryTest):
    """docstring for test_output_url"""

    # TODO: Let's mock is_valid_signature to return false here
    def test_rises_error_url_from_non_verified_signature(self):
        self.assertRaises(URLError,self.checkurl.url_response,'http://non.valid/?url')

    def test_returns_string_when_validation_succeds(self):
        self.assertIsInstance(self.checkurl.url_response(self.valid_url), str)

    def test_returns_full_query_string(self):
        expected_query = ('?firstname=First&lastname=Last&hash= '
            '4f6536ca2a23592d9037a4707bb44980b9bd2d4250fc1c833812068ccb000712')
        self.assertEqual(self.checkurl.url_response(self.valid_url), expected_query)