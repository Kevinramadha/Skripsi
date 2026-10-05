#!/bin/bash
# render.sh in.pptx first last outprefix
python3 -c "
import sys; sys.path.insert(0,'/tmp/pptwork/v5')
from single import make_subset
make_subset('$1', list(range($2,$3+1)), '/tmp/pptwork/v6/_sub.pptx')"
rm -f /tmp/pptwork/v6/r/_sub.pdf
soffice --headless --convert-to pdf --outdir /tmp/pptwork/v6/r /tmp/pptwork/v6/_sub.pptx >/dev/null 2>&1
rm -f /tmp/pptwork/v6/r/$4-*.png
pdftoppm -r 55 -png /tmp/pptwork/v6/r/_sub.pdf /tmp/pptwork/v6/r/$4
ls /tmp/pptwork/v6/r/$4-*.png | wc -l
