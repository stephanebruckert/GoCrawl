### install


#### 1. software needed

    easy_install pip
    pip install --upgrade pip
    pip install virtualenv

#### 2. prerequisites

    virtualenv env
    pip install -r ./requirements.txt

#### 3. run
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
