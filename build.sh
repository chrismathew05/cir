#!/bin/bash
# This script provides three options: 
#   1) generate + display docs [./build.sh "docs"]
#   2) run scratch file [./build.sh "z"],
#   3) run unit tests [./build.sh] 

echo Saving requirements...
source venv/bin/activate
pip freeze > requirements-prod.txt

if [[ $1 = "docs" ]]
then

  echo Building docs...
  cd docs
  make html
  cd build/html
  explorer.exe index.html
else
  if [[ $1 = "z" ]]
  then
    echo Running scratch file...
    cd app
    python3 z.py
  else
    echo Running unit tests...
    python -m unittest
  fi
fi