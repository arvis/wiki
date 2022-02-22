import re
from django.urls import reverse

def parse_string(str_to_parse):
    found_links = re.findall(r"\[([A-Za-z0-9_]+)\]", str_to_parse)
    parsed_string = str_to_parse
    
    for link in found_links:
        url = ''
        parsed_string = re.sub(f"\[{link}\]", f'<a href="{link.lower()}">{link}</a>', parsed_string)

    return parsed_string
    