A well-written README provides essential information about your project,
such as installation instructions, usage examples, and contributions guidelines.

List of usefull commands (all command should run under project root/working-directory):

# On first run:
```bash 
#create virtual environment (serve only this project):
python -m venv venv
#activate virtual environment
.\venv\Scripts\activate 
+ (venv) should appear as prefix to all command (run next command just after activating venv)
#update venv's python package-installer (pip) to its latest version
pip install --upgrade pip
#install projects packages
pip install -e .[dev]     
``` 

# Add/Remove/Re-install external modules/packages:
## Add new package:
1. add package to pyproject.toml
2. run 
```bash 
pip install -e .[dev]
``` 

## Remove new package:
1. remove the package from pyproject.toml
2. run:
```bash 
pip uninstall <package-name>
```
note: if you're don't remember the exact package name copy it from: 
```bash
pip list
```

# In case of a package failure (installation stoped in the middle or something like that):
1. delete venv file 
2. return on 'On first run' steps


# Health check:
### Check formatting, type hinting, lint code & docstrings:
Lint Project:
```bash
tox run -e lint
```
### Test Project: run all tests on diffrent python versions and produce tests-coverage and tests-results reports (make sure tested versions installed before run):
```bash
tox run -f test
```
## Lint and Test Project (on diffrent python versions):
```bash
tox run
```

# Not implemented yet (expand if needed):
- Build documentation:
```bash
tox run -e docs
```
- Packaging Python Project
```bash
tox run -e build
```