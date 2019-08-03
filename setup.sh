pip install -r requirements.txt
pip3 list -o --format columns|  cut -d' ' -f1|xargs -n1 pip install -U
pip freeze > requirements.txt
python manage.py migrate
