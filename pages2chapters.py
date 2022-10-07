import sys
import os
import re
from datetime import datetime

local_build = len(sys.argv) > 1 and sys.argv[1] == 'local'

md_link = re.compile('\[([^\]]+)\]\(([^ )]+)')
page_directory = 'pages'
output_path = sys.argv[1]

def rewrite_link(match):
    text, link = match.groups()
    internal = link.endswith('.md') and not link.startswith('http')
    if internal:
        fragment_link = '#' + link[:-3].replace('%20', '-')
        print(f"  Page link: {fragment_link}")
        return f'[{text}]({fragment_link}'
    else:
        print(f"  External link: {link}")
        return f'[{text}]({link}'

if os.path.exists(output_path):
    os.unlink(output_path)

pages = [pn for pn in os.listdir(page_directory) if pn.endswith('.md')]
pages.sort()
pages.remove("Welcome.md")
pages.insert(0, "Welcome.md")

for page_filename in pages:
    page_filename_url = page_filename.replace(' ', '%20')
    page_title = os.path.splitext(page_filename)[0]
    page_path = os.path.join(page_directory, page_filename)
    page_slug = page_title.replace(' ', '-')
    print(page_title)

    with open(output_path, 'a') as output_file:
#        output_file.write(f"# <a id=\"{page_slug}\"> {page_title}\n")
        output_file.write('# ' + page_title + ' {#' + page_slug + '}\n\n')
        page_text = open(page_path).read()
        if page_text.strip() == "":
            output_file.write("This page is [empty](#Empty%20page)\n")
        else:
            output_file.write(md_link.sub(rewrite_link, page_text))
        output_file.write("\n\n")

