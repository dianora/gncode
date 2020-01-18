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
And then activate it with
```
source .venv36/bin/activate
```

You may install the required python dependencies with
```
pip install -r requirements.txt
```

## Compiling the website
This site uses Jinja2 templates. The  following script compiles all templates under `templates`, and generate corresponding html files under `docs`.
```
python compile.py
```

