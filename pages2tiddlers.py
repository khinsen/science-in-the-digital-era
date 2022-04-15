import sys
import os
import re
from datetime import datetime

local_build = len(sys.argv) > 1 and sys.argv[1] == 'local'

md_link = re.compile('\[(.+)\]\(([^ ]+)(?: "(.+)")?\)')
page_directory = 'pages'
tiddler_directory = 'tiddlers'

def rewrite_link(match):
    text, link, _ = match.groups()
    if link.endswith('.md'):
        tw_link = '#' + link[:-3]
        return f'[{text}]({tw_link})'
    else:
        return f'[{text}]({link})'

for tiddler_file in os.listdir(tiddler_directory):
    os.unlink(os.path.join(tiddler_directory, tiddler_file))

for page_filename in os.listdir(page_directory):
    if not page_filename.endswith('.md'):
        continue
    page_title = os.path.splitext(page_filename)[0]
    print(page_title)

    page_path = os.path.join(page_directory, page_filename)
    meta_path = os.path.join(page_directory, page_filename + '.meta')
    tiddler_path = os.path.join(tiddler_directory, page_filename)
    meta_tiddler_path = os.path.join(tiddler_directory, page_filename + '.meta')

    stream = os.popen('git log --format=%at -- "' + page_path + '"')
    timestamps = stream.readlines()
    stream.close()
    if len(timestamps) == 0 and local_build:
        timestamps.append(os.path.getmtime(page_path))

    tw_timestamps = [datetime.fromtimestamp(int(timestamp)).strftime('%Y%m%d%H%M%S%f')[:-3] for timestamp in timestamps]
    tw_creation_timestamp = tw_timestamps[-1]
    tw_modification_timestamp = tw_timestamps[0]

    with open(tiddler_path, 'w') as tiddler_file:
        tiddler_file.write(md_link.sub(rewrite_link, open(page_path).read()))

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

