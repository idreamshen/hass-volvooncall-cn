import hashlib
import hmac
import urllib.parse
from urllib.parse import urlparse
from datetime import datetime

def hmac_sha256(key, msg):
    return hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()

def hex_encode_sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def urlencode(string):
    return urllib.parse.quote(string, safe='')

def find_header(headers, name):
    for key, value in headers.items():
        if key.lower() == name.lower():
            return value
    return None

def canonical_request(req, signed_headers):
    payload_hash = find_header(req['headers'], 'x-sdk-content-sha256')
    if payload_hash is None:
        payload_hash = hex_encode_sha256_hash(req['body'] if req['body'] else '')

    canonical_uri = '/'.join(urlencode(p) for p in req['uri'].split('/'))
    if not canonical_uri.endswith('/'):
        canonical_uri += '/'

    query_string = sorted((k, v) for k, v in req['query'].items())
    canonical_query_string = '&'.join(f"{urlencode(k)}={urlencode(v)}" for k, v in query_string)

    canonical_headers = '\n'.join(f"{k}:{v.strip()}" for k in signed_headers for v in [req['headers'].get(k, '')])
    if canonical_headers:
        canonical_headers += '\n'

    return f"{req['method']}\n{canonical_uri}\n{canonical_query_string}\n{canonical_headers}\n{';'.join(signed_headers)}\n{payload_hash}"

def string_to_sign(canonical_req, date_stamp, service='SDK-HMAC-SHA256'):
    return f"{service}\n{date_stamp}\n{hex_encode_sha256_hash(canonical_req)}"

def create_signature(string_to_sign, secret_key):
    return hmac_sha256(secret_key, string_to_sign)

def format_auth_header(signature, access_key, signed_headers):
    return f"SDK-HMAC-SHA256 Access={access_key}, SignedHeaders={';'.join(signed_headers)}, Signature={signature}"

def generate_date_stamp():
    return datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

def sign_request(url, method, body):
    parsed_url = urlparse(url)
    request = {
        'headers': {
            "x-sdk-content-sha256": "UNSIGNED-PAYLOAD",
            "host": "apigateway.digitalvolvo.com"
        },
        'method': "POST",
        'body': body,
        'uri': parsed_url.path,
        'host': "apigateway.digitalvolvo.com",
        'query': {}
    }
    key = "204114990"
    secret = "bjGqb3TvEEZ8W8QhoyhEH4IenwCnc4JQ"
    date = find_header(request['headers'], 'x-sdk-date')
    if date is None:
        date = generate_date_stamp()
        request['headers']['x-sdk-date'] = date

    if request['method'] not in ['PUT', 'PATCH', 'POST']:
        request['body'] = ''

    canonical_req = canonical_request(request, sorted([k.lower() for k in request['headers']]))
    string_to_sign_val = string_to_sign(canonical_req, date)
    signature = create_signature(string_to_sign_val, secret)

    return {
        'x-sdk-date':  request['headers']['x-sdk-date'],
        'v587sign': format_auth_header(signature, key, [k.lower() for k in request['headers']])
    }
