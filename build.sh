rm -rf build dist;
pip3 install virtualenv;
virtualenv -p python3 env;
source env/bin/activate;
pip install -r requirements.txt;
python setup.py py2app;
cp -r -f dist/main.app ~/Desktop;
# deactivate;
# rm -rf env;
