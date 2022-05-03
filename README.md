# canyon-notifier
---

### Pre-requirements
- [redis server up and running](https://redis.io/docs/getting-started/installation/)
- [python 3.9+](https://www.python.org/downloads/)

### Local setup
```shell
$ git clone git@github.com:Eira/canyon-notifier.git
$ cd canyon-notifier
$ python3.9 -m venv venv
$ source venv/bin/activate
$ pip install poetry
$ poetry install
```



### Local run tests
```shell
$ pytest
```