# Canyon notifier telegram bot
[CanyonNotifier](https://t.me/CanyonNotifierBot)

---
[![tests](https://github.com/Eira/canyon-notifier/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/Eira/canyon-notifier/actions/workflows/tests.yml)


### Pre-requirements
- [redis server up and running](https://redis.io/docs/getting-started/installation/)
- [python 3.9+](https://www.python.org/downloads/)

### Local setup
```shell
$ git clone git@github.com:Eira/canyon-notifier.git
$ cd canyon-notifier
$ python3.9 -m venv venv
$ source venv/bin/activate
$ pip install -U poetry pip setuptools
$ poetry config virtualenvs.create false --local
$ poetry install
```

Create env file to override default config
```bash
cat > .env << EOF
throttling_time=10.0
debug=true
redis_dsn= redis://localhost:6379/1
amount_of_iterations=2
bot_token=5435048925:AAE0CdbhQL7baW-EZmtVZ0nbyNbEtCQWUcE
EOF
```

### Local run tests
```shell
$ pytest --cov=app
```

### Local run app
```
python -m app.catalog_updater
```

### Local run flake
```
poetry run flake8 app/
```
### Local run MyPy
```
poetry run mypy app/
```

### Local run Telegram bot
```
python -m app.bot
```



