# gunicorn.conf.py
# Usage: gunicorn -c gunicorn.conf.py config.wsgi:application

bind = "0.0.0.0:8000"
workers = 2
worker_class = "sync"
timeout = 120
accesslog = "-"
errorlog = "-"
loglevel = "info"
