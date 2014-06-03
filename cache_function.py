import time
import memcache
import hashlib

def memorize(f):

    def newfn(*args, **kwargs):
        mc = memcache.Client(['127.0.0.1:11211'], debug=0)
        # generate md5 out of args and function
        m = hashlib.md5()
        margs = [x.__repr__() for x in args]
        mkwargs = [x.__repr__() for x in kwargs.values()]
        map(m.update, margs + mkwargs)
        m.update(f.__name__)
        m.update(f.__class__.__name__)
        key = m.hexdigest()

        value = mc.get(key)
        if value:
            return value
        else:
            value = f(*args, **kwargs)
            mc.set(key, value, 60 * 60 * 24 * 30)   # cached for a month!
            return value
        return f(*args)

    return newfn