

import hashlib
from urllib import parse
from urllib.error import URLError


ENCODING = 'cp1252'

def _extract(given_url):
    try:
        query = parse.urlparse(given_url).query
        data = parse.parse_qs(query, encoding = ENCODING,
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
        values.append(input_secret)
        # Based on the assignment example format to calculate signature
        # join values separated by '&' simbol
        asembly = "&".join(values) + '&'
        encoded = asembly.encode(ENCODING)
        # We add the input_secret before hash calculation.
        calculated_signature = hashlib.sha256(encoded)
        return calculated_signature.hexdigest() == B02K_MAC
    return False

def url_response(incoming_url):
    
    raise URLError(reason="Bad Request -Invalid URL")