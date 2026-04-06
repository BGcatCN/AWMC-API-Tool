import argparse
import json
import os
import sys
from urllib import request, parse


def parse_headers(header_list):
    headers = {}
    for header in header_list or []:
        if ':' not in header:
            continue
        name, value = header.split(':', 1)
        headers[name.strip()] = value.strip()
    return headers


def build_body(data_text, json_text):
    if json_text is not None:
        try:
            body = json.dumps(json.loads(json_text)).encode('utf-8')
        except json.JSONDecodeError as exc:
            raise ValueError(f'Invalid JSON payload: {exc}')
        return body, 'application/json'
    if data_text is not None:
        body = parse.urlencode(parse.parse_qsl(data_text)).encode('utf-8')
        return body, 'application/x-www-form-urlencoded'
    return None, None


def load_env_variable(filename, key):
    if not os.path.exists(filename):
        raise FileNotFoundError(f'Env file not found: {filename}')

    with open(filename, encoding='utf-8') as env_file:
        for line in env_file:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            name, value = line.split('=', 1)
            if name.strip() == key:
                return value.strip().strip('"').strip("'")

    raise KeyError(f'{key} not found in {filename}')


def main():
    parser = argparse.ArgumentParser(description='Simple Python API request helper')
    parser.add_argument('url', nargs='?', default=None, help='Request URL (optional; default is upload_b50 endpoint)')
    parser.add_argument('-X', '--method', default='GET', help='HTTP method (GET, POST, PUT, DELETE, etc.)')
    parser.add_argument('-H', '--header', action='append', help='Header in the form "Name: value"', metavar='HEADER')
    parser.add_argument('-d', '--data', help='Form data as key=value&key2=value2')
    parser.add_argument('-j', '--json', help='JSON body as string')
    parser.add_argument('-t', '--timeout', type=float, default=15.0, help='Request timeout in seconds')
    parser.add_argument('--upload-b50', action='store_true', help='Use the AWMC B50 upload endpoint (default when URL is omitted)')
    parser.add_argument('--qr-text', help='qr_text parameter for the upload endpoint')
    parser.add_argument('--env-file', default='.env', help='Path to the .env file containing FISH_TOKEN and BEARER_TOKEN')
    args = parser.parse_args()

    use_default_endpoint = args.upload_b50 or not args.url
    if use_default_endpoint:
        qr_text = args.qr_text
        if not qr_text:
            qr_text = input('请输入扫描二维码后的文本: ').strip()
            if not qr_text:
                raise ValueError('qr_text is required for upload_b50')

        fish_token = load_env_variable(args.env_file, 'FISH_TOKEN')
        args.url = f'https://api.awmc.cc/v1/upload_b50?qr_text={parse.quote(qr_text)}&fish_token={parse.quote(fish_token)}'
        args.method = 'GET'
        args.data = None
        args.json = None

    if not args.url:
        raise ValueError('Request URL is required')

    bearer_token = load_env_variable(args.env_file, 'BEARER_TOKEN')
    headers = parse_headers(args.header)
    if not any(name.lower() == 'authorization' for name in headers):
        headers['Authorization'] = f'Bearer {bearer_token}'

    body, content_type = build_body(args.data, args.json)

    if content_type and 'Content-Type' not in headers:
        headers['Content-Type'] = content_type

    req = request.Request(args.url, data=body, method=args.method.upper(), headers=headers)

    try:
        with request.urlopen(req, timeout=args.timeout) as response:
            resp_bytes = response.read()
            charset = response.headers.get_content_charset('utf-8')
            text = resp_bytes.decode(charset, errors='replace')
            print(f'Status: {response.status} {response.reason}')
            print('--- Response Headers ---')
            for name, value in response.getheaders():
                print(f'{name}: {value}')
            print('\n--- Response Body ---')
            try:
                parsed = json.loads(text)
                print(json.dumps(parsed, indent=2, ensure_ascii=False))
            except json.JSONDecodeError:
                print(text)
    except ValueError as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(1)
    except KeyError as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f'Request failed: {exc}', file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()
