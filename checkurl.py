#!/usr/bin/python3.9

import hashlib
import os
from urllib import parse
from urllib.error import URLError

# Constant variables
ENCODING = 'cp1252'
# We better not hard-code the secret
INPUT_SECRET = os.environ.get('SECRET_IN')
OUTPUT_SECRET = os.environ.get('SECRET_OUT')
# TODO: consider changing the following functions in to class methods


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

def is_valid_signature(given_url):
    extracted_data = _extract(given_url)
    if extracted_data:
        B02K_MAC = extracted_data.popitem()[1][0].lower()
        # Unpack data values
        values = [value[0] for value in extracted_data.values()]
        # We add the input_secret before hash calculation.
        values.append(INPUT_SECRET)
        # Based on the assignment example format to calculate signature
        # join values separated by '&' simbol
        asembly = "&".join(values) + '&'
        encoded = asembly.encode(ENCODING)
        calculated_signature = hashlib.sha256(encoded)
        return calculated_signature.hexdigest() == B02K_MAC
    return False

# TODO: This query assembly looks ugly. Let's refactor
def url_response(incoming_url):
    if is_valid_signature(incoming_url):
        query = parse.urlparse(incoming_url).query
        data = parse.parse_qs(query, encoding = ENCODING,
            keep_blank_values = True
            )
        firstname, lastname = data['B02K_CUSTNAME'][0].title().split()
        hash_calculation_string = '&'.join([
            f'firstname={firstname}',
            f'lastname={lastname}',
            ]
        )
        hash_calculation_string += f'#{OUTPUT_SECRET}'
        encoded = hash_calculation_string.encode(ENCODING)
        calculated_signature = hashlib.sha256(encoded)
        return '?'+hash_calculation_string.split('#')[0]+'&hash='+calculated_signature.hexdigest()

    raise URLError(reason="Bad Request -Invalid URL")



if __name__ == '__main__':
    # Test purpose secrets:
    INPUT_SECRET = 'inputsecret'
    OUTPUT_SECRET = 'outputsecret'
    url = input('Enter a valid URL: ')
    print('\nYour new signed URL is: ' + url_response(url))