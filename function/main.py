import requests
from flask import Request

import sni_processor


def webhook(request: Request):
    request_headers = request.headers
    body = request.get_data(as_text=True)
    forward_url = request_headers['FORWARD_URL']
    forward_fqdn = request_headers['FORWARD_FQDN']
    forward_headers = {
        'content-type': request_headers['content-type'],
        'Authorization': request_headers['FORWARD_Authorization']
    }
    session = requests.Session()
    session.mount("https://", sni_processor.HostHeaderSSLAdapter(forward_fqdn))
    return session.post(forward_url, body, headers=forward_headers).text
