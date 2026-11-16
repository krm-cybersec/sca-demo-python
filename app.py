import sys
import requests
from jinja2 import template

def main():
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    resp = requests.get(url, auth=("demo","demo-password"), timeout=10)
    print(Template("Status for {{url}}: {{code}}").render(url=url,code=resp.status_code))

if __name__ == "__main__":
    main()