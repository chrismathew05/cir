echo Saving requirements...
source venv/bin/activate
pip freeze > requirements.txt

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