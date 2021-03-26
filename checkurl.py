

import hashlib


ERROR_URL = 'http://error'

def extract(given_url):
    return {i:2*i for i in range(10)}

def valid_signature(given_url):
    # B02K_VERS, B02K_TIMESTMP, B02K_IDNBR, 
    # B02K_STAMP, B02K_CUSTNAME, B02K_KEYVERS, 
    # B02K_ALG, B02K_CUSTID, B02K_CUSTTYPE, B02K_MAC
    extracted_data = extract(given_url)
    B02K_MAC = extracted_data.popitem()
    encoded = "".join(extracted_data.values()).encode('cp1252')
    calculated_signature = hashlib.sha256(encoded)
    return False