#!/usr/bin/env python

import re

def dependencies():
    pass

def tamper(payload, **kwargs):
    #Returns string in utf-8 format ex 'ab'-> '\u0061\u0062'

    encoded_payload = ""
    payload = bytes(payload, encoding='utf-8')
    for x in payload:
        encoded_payload = encoded_payload + "\\" + hex(x)

    return (re.sub("0x", "u00", encoded_payload))
