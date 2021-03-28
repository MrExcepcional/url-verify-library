# Url-Verify-Library
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg?style=for-the-badge&logo=appveyor)](https://www.python.org/downloads/release/python-392/)

This library is a solved code challenge to implement an unit tested URL signature validation. Parses certain details from the query string and returns a new signed URL with different query string.

## 📦 Installation

Use of python3.9 recommended. You can find it [here](https://www.python.org/downloads/release/python-392/)

## 🚀 How to use

In command line run 
```bash
python3.9 checkurl.py
```
A valid URL is in the format `http://domain.com/?B02K_VERS=0003&B02K_TIMESTMP=50020181017141433899056&B02K_IDNBR=2512408990&B02K_STAMP=20010125140015123456&B02K_CUSTNAME=FIRST%20LAST&B02K_KEYVERS=0001&B02K_ALG=03&B02K_CUSTID=9984&B02K_CUSTTYPE=02&B02K_MAC=EBA959A76B87AE8996849E7C0C08D4AC44B053183BE12C0DAC2AD0C86F9F2542`

To run tests
```bash
python3.9 -m unittest test_library
```