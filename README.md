## Fridagar.is API

iCalendar python module: https://pypi.python.org/pypi/icalendar/2.1

```sh
$ pip install icalendar
```

Flask python module: http://flask.pocoo.org

```sh
$ pip install Flask
```

And we're using memcached to cache holidays: https://pypi.python.org/pypi/python-memcached/1.53

Install and run:

```sh
$ tar xzf python-memcached-1.53.tar.gz
$ cd python-memcached-1.53
$ python setup.py install
$ memcached
```