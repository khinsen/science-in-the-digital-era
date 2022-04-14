import sys
import os
import re
from datetime import datetime

md_link = re.compile('\[(.+)\]\(([^ ]+)(?: "(.+)")?\)')
page_directory = 'pages'
tiddler_directory = 'tiddlers'

def rewrite_link(match):
    text, link, _ = match.groups()
    tw_link = '#' + link[:-3]
    return f'[{text}]({tw_link})'

for tiddler_file in os.listdir(tiddler_directory):
    os.unlink(os.path.join(tiddler_directory, tiddler_file))

for page_file in os.listdir(page_directory):
    page_title = os.path.splitext(page_file)[0]
    print(page_title)
    page_text = open(os.path.join(page_directory, page_file)).read()
    stream = os.popen('git log --format=%at -- "' + os.path.join(page_directory, page_file) + '"')
    timestamps = stream.readlines()
    stream.close()
    tw_timestamps = [datetime.fromtimestamp(int(timestamp)).strftime('%Y%m%d%H%M%S%f')[:-3] for timestamp in timestamps]
    tw_creation_timestamp = tw_timestamps[-1]
    tw_modification_timestamp = tw_timestamps[0]
    with open(os.path.join(tiddler_directory, page_file), 'w') as tiddler_file:
        tiddler_file.write(md_link.sub(rewrite_link, page_text))
    with open(os.path.join(tiddler_directory, page_title + '.meta'), 'w') as meta_file:
        meta_file.write(f'title: {page_title}\n')
        meta_file.write(f'created: {tw_creation_timestamp}\n')
        meta_file.write(f'modified: {tw_modification_timestamp}\n')
        meta_file.write('type: text/x-markdown\n')

