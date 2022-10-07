python3 pages2chapters.py all.md
pandoc -f markdown+header_attributes -t pdf all.md -o all.pdf -s \
   --top-level-division=chapter \
   -V colorlinks=true \
   -V linkcolor=blue \
   -V urlcolor=magenta
