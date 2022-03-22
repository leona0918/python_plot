## Common Steps/Concept Why Use Python Virtual Environment
```showLineNumbers
mkdir my_new_project
cd my_new_project
python3 -m venv .venv # <- This will create a new virtual environment in `.venv`
nano requirements.txt # <- create a new file where each line contains one dependency (prefered with version), e.g.: numpy==1.22.3
.venv/bin/pip install -r requirements.txt
```
>Professor K
>>If you change your requirements.txt just run .venv/bin/pip install -r requirements.txt again.
this will ensure that each projects has their own dependencies and if something goes wrong you can just rm -rf .venv (but keep the requirements.txt) and start fresh.
also different projects can have the dependencies in different versions
but Python is already a mess, even XKCD made a commic of it: https://xkcd.com/1987/
## Mac OS
- Install virtual environment
```
cd path/to/your/project
python3 -m venv .venv
```
- Install packages listed in file 'requirements.txt'
```
.venv/bin/pip install -r requirements.txt
```

## Window 10
- Run command (cmd) to install virtual environment
```
cd path/to/your/project/
python -m venv ./.venv
```
- Activate virtural environment
```
cd .venv
activate
```
- Install packages listed in file 'requirements.txt'
```
Scripts\pip.exe install -r ../requirements.txt
```

### Other commands, working directory is .venv
If need to upgrade pip version
```
Scripts/python.exe -m pip install --user --upgradge pip
```
Check python/pip path
```
whereis python
whereis pip
```

## Ubuntu 
TODO