A well-written README provides essential information about your project,
such as installation instructions, usage examples, and contributions guidelines.

list of usefull commands:

#install all the packages required for development
pip install --upgrade pip
pip install -e .[dev] 

#list all installed packages
pip list

#lint your project
tox run -e lint

#build project's documentation 
tox run -e docs

#package the project (make project a package)
tox run -e build

#run all files with the word 'test' in it
tox run -f test

#check project's health (on diffrent python versions)
tox run

#create  HTML tests reports
pytest . --html=reports/report.html
pytest --cov --cov-report=html:reports/coverage

