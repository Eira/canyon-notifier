# [Canyon notifier telegram bot](https://t.me/CanyonNotifierBot)

[![tests](https://github.com/Eira/canyon-notifier/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/Eira/canyon-notifier/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/Eira/canyon-notifier/branch/master/graph/badge.svg?token=4D3V7NMX9Q)](https://codecov.io/github/Eira/canyon-notifier)
[![linters](https://github.com/Eira/canyon-notifier/actions/workflows/linters.yml/badge.svg?branch=master)](https://github.com/Eira/canyon-notifier/actions/workflows/linters.yml)

Telegram bot that shows actual catalog of available bicycles at [canyon.com](https://www.canyon.com).

You can also subscribe to a newsletter when a particular model or family of bikes becomes available.

[vas3k.club post](https://vas3k.club/thread/18283/#comment-25634871-b9d2-4cb4-9359-2b38ac818446) 
[vc.ru post](https://vc.ru/tribuna/618090-subbotniy-samopiar-na-vc-ru?comment=5573937&from=copylink&type=quick) 

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

### Local run Telegram bot
```
python -m app.bot_runner
```

### Local run catalog updater
```
python -m app.catalog_updater
```

### Local run subscription notifier
```
python -m app.subscription_notifier
```

### Local run tests
```shell
$ pytest --cov=app
```

### Local run linters
```
poetry run flake8 app/

poetry run mypy app/
```

