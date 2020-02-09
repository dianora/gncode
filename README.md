# gncode.org website
## Structure
- `tempates`: HTML page templates (with Jinga2 templating language)
- `docs`: Compiled templates  and static web content
- `requirements.txt`: Python dependencies
- `compile.py`: Compiles the website

##  Working environment
Python virtual environments are recommended  when working with this repository. With python 3.6 you may create one as follow:
```
python3.6 -m venv .venv36
```
and then activate it with:
```
source .venv36/bin/activate
```

You may install the required python dependencies with:
```
pip install -r requirements.txt
```

## Localization and internationalization
This site uses Babel and its Jinga's integration for localisation and internationalization.
Here are useful scripts

### Maintaining translations
- 
```
pybabel extract -F babel.cfg -o messages.pot .
```
- Updating translations
This will synchronize the message ids from `messages.pot` generated above to each of the translation files
```
pybabel update -i messages.pot -d translations/
```
- Compiling translations
```
pybabel compile -d translations/
```

### Creating new translations
This is only needed when adding support for a new language.
#### Creating a translation for English (en)
This initializes language files for English. Refer to the "Maintaining  translations" section for next steps.
```
pybabel init -i messages.pot -d translations -l en
```
####  Updating the language menu
Update templates/index.html, and add a new item to the language drop down menu. Here is an example:
```
<a class="dropdown-item" data-gncode-lang='en'>English</a>
````

## Compiling the website
This site uses Jinja2 templates. The following script compiles all templates under `templates`, and generate corresponding html files under `docs/<lang>` for each langugage
```
python compile.py
```

