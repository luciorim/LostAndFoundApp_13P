1. clone the project
```
git clone https://github.com/luciorim/lost-and-found-uni.git
```
3. create venv

  for Windows 
```
python -m venv venv
venv\Scripts\activate
```
  for MacOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```

3. go to project directory
```
cd lost-and-found-uni
```

5. install requirements
```
pip install -r requirements.txt
```
7. run server (Check that port :8000 is free)
```
python/python3 manage.py runserver
