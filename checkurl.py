

import hashlib
from urllib import parse


ERROR_URL = 'http://error'

def _extract(given_url):
    try:
        query = parse.urlparse(given_url).query
        data = parse.parse_qs(query, encoding = 'cp1252',
            keep_blank_values = True
            )
        return data
    except Exception as e:
        print(e)
        return False

def is_valid_signature(given_url, input_secret):
    extracted_data = _extract(given_url)
    if extracted_data:
        B02K_MAC = extracted_data.popitem()[1][0].lower()
        # Unpack data values
        values = [value[0] for value in extracted_data.values()]
        # Based on the assignment example format to calculate signature
        # join values separated by '&' simbol
        asembly = "&".join(values) + input_secret
        encoded = asembly.encode("cp1252")
        # We add the input_secret before hash calculation.
        calculated_signature = hashlib.sha256(encoded)
        return calculated_signature.hexdigest() == B02K_MAC
    return False