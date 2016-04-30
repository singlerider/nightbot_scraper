# Nightbot Scraper
'Cause why not?

## Installation
### Virtual Environment
I would recommend running this in a virtual environment to keep your dependencies in check. If you'd like to do that, run:

```shell
sudo pip install virtualenv
```

Followed by:

```shell
virtualenv venv
```

This will create an empty virtualenv in your project directory in a folder called "venv." To enable it, run:

```shell
source venv/bin/activate
```

and your console window will be in that virtualenv state. To deactivate, run:

```shell
deactivate
```

### Dependencies
To install all dependencies locally (preferably inside your activated virtualenv), run:

```shell
pip install -r requirements.txt
```

If you'd like to use PhantomJS, you'll need to install it. You can find instructions for doing so at http://phantomjs.org/

## To Run
```shell
python scraper.py ChannelNameGoesHere
```

The script will print a list of command objects and the number identified.

