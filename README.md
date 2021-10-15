# On Windows
    python -m venv venv
    venv\Scripts\activate.bat
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

# On Linux or Mac OS 
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 manage.py migrate
    python3 manage.py runserver
