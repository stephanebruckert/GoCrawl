### install

    pip install --upgrade pip
    pip install virtualenv
    pip install -r ./requirements.txt
    python main.py

### options

 - TODO options:
 - vertical?/horizontal? - tail/head
 - speed?
 - allow subdomains?
 - display progress?

### choices

 - python2.7
 - BeautifulSoup because:
   - we don't need to be that fast,
   - saves development time,
   - more forgiving towards unknown and potentially corrupt source.
