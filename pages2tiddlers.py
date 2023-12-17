import sys
import os
import re
from datetime import datetime

local_build = len(sys.argv) > 1 and sys.argv[1] == 'local'

md_link = re.compile('\[([^\]]+)\]\(([^ )]+)')
page_directory = 'pages'
tiddler_directory = 'tiddlers'

def rewrite_link(match):
    text, link = match.groups()
    internal = link.endswith('.md') and not link.startswith('http')
    if internal:
        tw_link = '#' + link[:-3]
        print(f"  Page link: {tw_link}")
        return f'[{text}]({tw_link}'
    else:
        print(f"  External link: {link}")
        return f'[{text}]({link}'

for tiddler_file in os.listdir(tiddler_directory):
    os.unlink(os.path.join(tiddler_directory, tiddler_file))

for page_filename in os.listdir(page_directory):
    if not page_filename.endswith('.md'):
        continue
    page_filename_url = page_filename.replace(' ', '%20')
    page_title = os.path.splitext(page_filename)[0]
    print(page_title)

    page_path = os.path.join(page_directory, page_filename)
    meta_path = os.path.join(page_directory, page_filename + '.meta')
    tiddler_path = os.path.join(tiddler_directory, page_filename)
    meta_tiddler_path = os.path.join(tiddler_directory, page_filename + '.meta')

    with os.popen('git log --format=%at -- "' + page_path + '"') as stream:
        timestamps = stream.readlines()
    if len(timestamps) == 0 and local_build:
        timestamps.append(os.path.getmtime(page_path))

    tw_timestamps = [datetime.fromtimestamp(int(timestamp)).strftime('%Y%m%d%H%M%S%f')[:-3] for timestamp in timestamps]
    tw_creation_timestamp = tw_timestamps[-1]
    tw_modification_timestamp = tw_timestamps[0]

    with os.popen('git log --format=%H') as stream:
        commits = stream.readlines()
    commit = commits[0].strip()

    with os.popen(f'git hash-object "{page_path}"') as stream:
        git_hash = stream.readlines()[0].strip()
    print("Page hash: ", git_hash)

    # Tiddler text
    with open(tiddler_path, 'w') as tiddler_file:
        page_text = open(page_path).read()
        if page_text.strip() == "":
            tiddler_file.write("This page is [empty](#Empty%20page)\n")
        else:
            tiddler_file.write(md_link.sub(rewrite_link, page_text))
        tiddler_file.write("\n<br>\n")
        tiddler_file.write("[Permanent link to this version]")
        tiddler_file.write(f"(https://codeberg.org/khinsen/science-in-the-digital-era/src/commit/{commit}/pages/{page_filename_url})")
        tiddler_file.write(" ([archive copy]")
        tiddler_file.write(f"(https://archive.softwareheritage.org/swh:1:cnt:{git_hash}))")
        tiddler_file.write("\n")

    # Metadata file
    if os.path.exists(meta_path):
        meta = []
        for line in open(meta_path):
            if line.split()[0] not in ['created:', 'modified:']:
                meta.append(line)
    else:
        meta = [f'title: {page_title}\n',
                'type: text/x-markdown\n']
    meta.append(f'created: {tw_creation_timestamp}\n')
    meta.append(f'modified: {tw_modification_timestamp}\n')
    with open(meta_tiddler_path, 'w') as meta_file:
        for line in meta:
            meta_file.write(line)

