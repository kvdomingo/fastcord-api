wsgi_app = "fastcord.wsgi"

pidfile = "/tmp/gunicorn.pid"

worker_class = "gevent"
workers = 2

errorlog = "-"
accesslog = "-"
loglevel = "debug"
capture_output = True
