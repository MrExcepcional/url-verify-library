

import hashlib


ERROR_URL = 'http://error'

def extract(given_url):
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

def valid_signature(given_url):
    # B02K_VERS, B02K_TIMESTMP, B02K_IDNBR, 
    # B02K_STAMP, B02K_CUSTNAME, B02K_KEYVERS, 
    # B02K_ALG, B02K_CUSTID, B02K_CUSTTYPE, B02K_MAC
    extracted_data = extract(given_url)
    B02K_MAC = extracted_data.popitem()
    encoded = "".join(extracted_data.values()).encode('cp1252')
    calculated_signature = hashlib.sha256(encoded)
    return False