source venv/bin/activate
pip freeze > requirements.txt

if [[ $1 = "docs" ]]
then

cd docs
make html
cd build/html
explorer.exe index.html

fi