import os
import src.libs.logger as logger
from redis import Redis

def parse_redis_url(url):
    tmp = url.replace('redis://', '').split('@')

    host = ''
    port = ''
    db = '1'
    password = ''

    aux2 = tmp[1].split('/')

    aux2[0] = aux2[0].split(':')

    host = aux2[0][0]
    port = aux2[0][1]

    if len(aux2) == 2:
        db = aux2[1]

    if len(tmp) > 1:
        aux1 = tmp[0].split(':')
        password = aux1[1] if len(aux1) == 2 else aux1[0]

    if len(tmp) == 0:
        password = None

    return host, port, db, password


host, port, db, password = parse_redis_url(os.environ.get('REDIS_URL'))

REDIS = Redis(
    host=host,
    port=port,
    db=db,
    password=password
)