VENV = .env

SIGAL = $(VENV)/bin/sigal

PELICAN = $(VENV)/bin/pelican
PELICAN_THEME = free-agent

SRC = source
CONTENT = content
DST = $(CONTENT)/images/portfolio
IMAGES = images
HTML = *.html
STATIC = static
AUTHOR = author
CATEGORY = category
FEEDS = feeds


all: requirements sigal-build pelican-build

venv:
	-@virtualenv $(VENV) --python=python3

requirements: venv
	@$(VENV)/bin/pip install -r requirements.txt

clean-output:
	@rm -fr $(IMAGES) $(HTML) $(STATIC) $(AUTHOR) $(CATEGORY) $(FEEDS)

clean-content:
	@rm -fr $(CONTENT)

clean-images:
	@rm -fr $(DST)

clean-venv:
	@rm -fr $(VENV)

distclean: clean-output clean-images clean-venv

sigal-init: requirements
	-@$(SIGAL) init

sigal-build:
	@$(SIGAL) build $(SRC) $(DST)

pelican-build:
	@$(PELICAN) -t $(PELICAN_THEME) -o .
