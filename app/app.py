from celery import Celery
from .config import REDIS_URL

app = Celery('DevCon',
             broker=REDIS_URL,
             backend=REDIS_URL,
             include=['tasks'])
