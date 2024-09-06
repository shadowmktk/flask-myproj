import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_connections = 1024
threads = 2

accesslog = "-"
errorlog = "-"

# https://docs.gunicorn.org/en/stable/settings.html#access-log-format
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %({x-forwarded-for}i)s %(M)s %(D)s'
