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

   [https://codeberg.org/khinsen/science-in-the-digital-era](https://codeberg.org/khinsen/science-in-the-digital-era)

This archival copy corresponds to
[commit {commit}](https://codeberg.org/khinsen/science-in-the-digital-era/src/commit/{commit}), which was published on {date}.

This digital garden contains essays, thoughts, random ideas, and references that relate to the practice of [scientific research in the digital era](#Science-in-the-digital-era), characterized by computers (personal, high-performance, cloud, ...), software, the Internet, global collaborations, social networks, and more. They represent exclusively [my personal views](#About-the-author) and in particular not those of [my employer](https://www.cnrs.fr/).

There are many empty pages in this collection, and you may wonder why.

One reason is that this digital garden is work in progress. When I work on a page, I often insert links to pages that I intend to write, but haven't written yet. So you see an empty page. If you come back later, you may find some real content there. So... come back often.

The second reason is that empty pages are useful link targets, due to the backlink feature in the online version of my digital garden. At the end of each page, you see a list of other pages that link to the current one. Empty pages thus fulfill the role of a subject index in a traditional book: they help you find where some topic is discussed. Unfortunately, this feature is lost in this archival copy.

### License

The pages of this digital garden are covered by the Creative Commons License [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

According to this license, you are free to:
- Share: copy and redistribute the material in any medium or format.
- Adapt: remix, transform, and build upon the material.

under the following conditions:
- Attribution: You must give appropriate credit.
- NonCommercial: You may not use the material for commercial purposes.
- ShareAlike: You must distribute your contributions under the same license.
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

