rm -rf build dist venv;
pip3 install virtualenv;
virtualenv -p python3 venv;
source venv/bin/activate;
pip install -r requirements.txt;
python setup.py py2app;
cp -r -f dist/APG\ LINK.app ~/Desktop;
deactivate;
rm -rf env;
