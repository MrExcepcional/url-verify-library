

import hashlib


ERROR_URL = 'http://error'

def _extract(given_url):
    try:
        # We just trim the leading domain
        raw_data = given_url.split('?')[1]
        # Then separate each data element
        raw_data = raw_data.split('&')
        # separate keys from values.
        # TODO: find better sintax for this block
        keys,values=[],[]
        for item in raw_data:
            key_value_tuple = item.split('=')
            keys.append(key_value_tuple[0])
            values.append(key_value_tuple[1])
        # Now store values and keys in a dict
        data = dict(zip(keys, values))
        return data
    except Exception as e:
        print(e)
        return False

def is_valid_signature(given_url):
    extracted_data = _extract(given_url)
    #if extracted_data:
    B02K_MAC = extracted_data.popitem()
    encoded = "".join(extracted_data.values()).encode('cp1252')
    calculated_signature = hashlib.sha256(encoded)
        #return calculated_signature == B02K_MAC
    return False