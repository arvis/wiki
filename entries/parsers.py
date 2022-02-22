import re
from django.urls import reverse

def parse_string(str_to_parse):
    found_links = re.findall(r"\[([A-Za-z0-9_]+)\]", str_to_parse)
    parsed_string = str_to_parse

    for link in found_links:
        url = reverse('view_entry', kwargs={'entry_title': link.lower()})
        parsed_string = re.sub(f"\[{link}\]", f'<a href="{url}">{link}</a>', parsed_string)

    return parsed_string
    