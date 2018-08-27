import calendar
import time
import src.libs.logger as logger

def join(l, separator):
    final = ''

    for i in l:
        if l.index(i) == 0:
            final = final + str(i)
        else:
            final = final + separator + str(i)

    return final

def parse_error(e):
    str_error = str(e)

    str_error = str_error.replace('\t', '').replace('    ', '')
    str_error = str_error.split('\n')

    while True:
        try:
            del str_error[str_error.index('')]
        except:
            break

    return str_error

def current_epoch():
    return calendar.timegm(time.gmtime())