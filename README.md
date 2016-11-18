# GoCrawl

## How to

All these commands can be ran from the current folder.

### Prerequisites

1. Make sure you run Python2.7
2. `easy_install pip`
3. `pip install --upgrade pip`

### Setting up a virtual environment (optional)

1. `pip install virtualenv`
2. `virtualenv env` to create a project-owned environment
3. `source env/bin/activate` to activate it

### Install required modules

`make` or `pip install -r ./requirements.txt`

### Run with options

    $ python main.py -h
    usage: main.py [-h] -L LINK [--silent] [-W WAIT]

    GoCrawl

    optional arguments:
      -h, --help            show this help message and exit
      -L LINK, --link LINK  Entry point URL
      --silent              Silent mode
      -W WAIT, --wait WAIT  Minimum wait time in seconds between each request

#### Examples:

- `python main.py -h`
- `python main.py -L http://google.fr`
- `python main.py -L http://google.fr --silent` to hide the progress outputs
- `python main.py -L http://google.fr --wait 5` to wait between each requests

### Tasks

- `make test` to run unit tests
- `make lint` to run linter

### Search rules

Search rules follow the format:

    'data_category':
      {
        'data_type':
                [
                  ['tag', 'condition_key', 'condition_value', 'source_attr'],
                  ['tag', 'condition_key', 'condition_value', 'source_attr']
                ]
      }
    },

Current rules to retrieve links, images, javascript and stylesheets are defined in the `Parser` class:

    {
        'next': {
            'url':    [['a', 'href', True, 'href']]
        },
        'assets': {
            'images': [['img', 'src', True, 'src']],
            'css':    [
                        ['link', 'rel', 'stylesheet', 'href'],
                        ['link', 'type', 'text/css', 'href'],
                        ['link', 'rel', 'stylesheet/less', 'href'],
                        ['link', 'rel', 'stylesheet/css', 'href']
                      ],
            'js':     [['script', 'src', True, 'src']]
        }
    }

### Sample output

    $ python main.py -L http://hackcss.com/
    Crawling http://hackcss.com/...
    http://hackcss.com/                                          Visited: 1        Remaining: 4       
    http://hackcss.com/standard.html                             Visited: 2        Remaining: 3       
    http://hackcss.com/dark.html                                 Visited: 3        Remaining: 2       
    http://hackcss.com/dark-grey.html                            Visited: 4        Remaining: 1       
    http://hackcss.com/solarized-dark.html                       Visited: 5        Remaining: 0       

    Done:
    {
      "failures": {
        "total": 0,
        "data": []
      },
      "success": {
        "total": 5,
        "data": [
          {
            "url": "http://hackcss.com/",
            "assets": {
              "images": [],
              "css": [
                "http://hackcss.com/prism.css",
                "http://hackcss.com/hack.css?t=1473587248285",
                "http://hackcss.com/site.css?t=1473587248285"
              ],
              "js": [
                "http://hackcss.com/app.js",
                "http://hackcss.com/prism.js"
              ]
            }
          },
          {
            "url": "http://hackcss.com/standard.html",
            "assets": {
              "images": [],
              "css": [
                "http://hackcss.com/site.css?t=1473587248285",
                "http://hackcss.com/prism.css",
                "http://hackcss.com/hack.css?t=1473587248285",
                "http://hackcss.com/standard.css?t=1473587248285"
              ],
              "js": [
                "http://hackcss.com/app.js",
                "http://hackcss.com/prism.js"
              ]
            }
          },
          {
            "url": "http://hackcss.com/dark.html",
            "assets": {
              "images": [],
              "css": [
                "http://hackcss.com/site-dark.css?t=1473587248285",
                "http://hackcss.com/prism.css",
                "http://hackcss.com/hack.css?t=1473587248285",
                "http://hackcss.com/dark.css?t=1473587248285",
                "http://hackcss.com/site.css?t=1473587248285"
              ],
              "js": [
                "http://hackcss.com/app.js",
                "http://hackcss.com/prism.js"
              ]
            }
          },
          {
            "url": "http://hackcss.com/dark-grey.html",
            "assets": {
              "images": [],
              "css": [
                "http://hackcss.com/site-dark.css?t=1473587248285",
                "http://hackcss.com/site.css?t=1473587248285",
                "http://hackcss.com/prism.css",
                "http://hackcss.com/hack.css?t=1473587248285",
                "http://hackcss.com/dark-grey.css?t=1473587248285"
              ],
              "js": [
                "http://hackcss.com/app.js",
                "http://hackcss.com/prism.js"
              ]
            }
          },
          {
            "url": "http://hackcss.com/solarized-dark.html",
            "assets": {
              "images": [],
              "css": [
                "http://hackcss.com/solarized-dark.css?t=1473587248285",
                "http://hackcss.com/site-dark.css?t=1473587248285",
                "http://hackcss.com/prism.css",
                "http://hackcss.com/hack.css?t=1473587248285",
                "http://hackcss.com/site.css?t=1473587248285"
              ],
              "js": [
                "http://hackcss.com/app.js",
                "http://hackcss.com/prism.js"
              ]
            }
          }
        ]
      }
    }
