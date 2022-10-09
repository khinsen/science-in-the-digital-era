python3 pages2chapters.py all.md
pandoc all.md \
       -f markdown+header_attributes+yaml_metadata_block \
       -t pdf -o all.pdf -s \
       --top-level-division=chapter \
       -V colorlinks=true \
       -V linkcolor=blue \
       -V urlcolor=magenta
