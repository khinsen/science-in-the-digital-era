import sys
import os
import re
from datetime import datetime

local_build = len(sys.argv) > 2 and sys.argv[2] == 'local'

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

with os.popen('git log --format="%H %ci" -1') as stream:
    commit_log = stream.readlines()
commit, date, time, tzone = commit_log[-1].split()

pages = [pn for pn in os.listdir(page_directory) if pn.endswith('.md')]
pages.sort()
pages.remove("Welcome.md")
#pages.insert(0, "Welcome.md")

if os.path.exists(output_path):
    os.unlink(output_path)

pdf_title = f"""
---
title: 'Science in the digital era'
author: Konrad Hinsen,
        Centre de Biophysique Moléculaire (CNRS, France)
date: {date}
---

"""

pdf_welcome = "# Welcome {#Welcome}" + f"""

This is an archival copy of my [digital garden](#Digital-Garden) whose
current on-line version can be consulted at

   [https://github.com/khinsen/science-in-the-digital-era](https://github.com/khinsen/science-in-the-digital-era)

This archival copy corresponds to
[commit {commit}](https://github.com/khinsen/science-in-the-digital-era/tree/{commit}), which was published on {date}.

This digital garden contains essays, thoughts, random ideas, and references that relate to the practice of [scientific research in the digital era](#Science-in-the-digital-era), characterized by computers (personal, high-performance, cloud, ...), software, the Internet, global collaborations, social networks, and more. They represent exclusively [my personal views](#About-the-author) and in particular not those of [my employer](https://www.cnrs.fr/).

### License

The pages of this digital garden are covered by a Creative Commons License ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) to be precise).


"""

with open(output_path, 'a') as output_file:
    output_file.write(pdf_title)
    output_file.write(pdf_welcome)

for page_filename in pages:
    page_filename_url = page_filename.replace(' ', '%20')
    page_title = os.path.splitext(page_filename)[0]
    page_path = os.path.join(page_directory, page_filename)
    page_slug = page_title.replace(' ', '-')
    print(page_title)

    with open(output_path, 'a') as output_file:
        output_file.write('# ' + page_title + ' {#' + page_slug + '}\n\n')
        page_text = open(page_path).read()
        if page_text.strip() == "":
            output_file.write("This page is [empty](#Empty-page)\n")
        else:
            output_file.write(md_link.sub(rewrite_link, page_text))
        output_file.write("\n\n")

