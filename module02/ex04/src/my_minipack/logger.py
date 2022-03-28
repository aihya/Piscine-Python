import time
import os


def log(__func):
    def wrapper(*args, **kwargs):
        username = os.environ.get('USER')

        action = ' '.join(__func.__name__.split('_')).title()

        t1 = time.time()
        result = __func(*args, **kwargs)
        t2 = time.time()
        dt = '{:.3f} '.format((t2 - t1) * 1000 if (t2 - t1) * 1000 < 1 else (t2 - t1))
        dt += 'ms' if (t2 - t1) * 1000 < 1 else 's'

        with open('actions.log', 'a') as logfile:
            logfile.write('({})Running: {:20}[ exec-time = {} ]\n'.format(username, action, dt))

        return result
    return wrapper
