## Redis Cashing in Django
this demo app contain a simple model name 
artical which can store only two attributes 
name and text in database . in this app we 
first fetch data from the database and at the 
same time we store it into the redis server 
and after that we get data from redis cash


## deployment
```bash
    sudo apt install docker.io
    sudo docker run -itp 6379:6379 --name run_reds redis 
    python -m venv django_install
    source ./django_install/bin/active
    git clone https://github.com/ahmadebtisam3/django-redis-chasing.git
    cd RedisCashing/
    pip install -r requirments.txt
    python manage.py runserver
```