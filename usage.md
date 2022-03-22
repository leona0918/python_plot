## Mac OS

## Window 10
- Run command (cmd) to install virtrual environment
```
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